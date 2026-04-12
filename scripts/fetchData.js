import fs from 'fs';
import path from 'path';
import { parse } from 'csv-parse/sync';

const TOOLS_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO-nmWXULh5Wnt08E4q_DnCOlK5ZbzeohCGFdHIbheY7T8EungTlS6XAADa87ECbYMajJ656xsGY7n/pub?gid=0&single=true&output=csv';
const IDEAS_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO-nmWXULh5Wnt08E4q_DnCOlK5ZbzeohCGFdHIbheY7T8EungTlS6XAADa87ECbYMajJ656xsGY7n/pub?gid=1978113116&single=true&output=csv';

async function fetchAndSave(url, keyMapping, outputFile) {
  try {
    console.log(`Fetching ${url}...`);
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    const csvData = await res.text();
    
    // Parse CSV
    const records = parse(csvData, {
      columns: true,
      skip_empty_lines: true,
      trim: true
    });
    
    // Map to JSON format our frontend expects
    const finalData = records.map(record => {
      const formatted = {};
      for (const [csvCol, jsonKey] of Object.entries(keyMapping)) {
        formatted[jsonKey] = record[csvCol] || '';
      }
      
      // Post-processing for arrays
      if (formatted.tags && typeof formatted.tags === 'string') {
        formatted.tags = formatted.tags.split(',').map(s => s.trim()).filter(Boolean);
      } else if (!formatted.tags) {
        formatted.tags = [];
      }
      
      if (formatted.features && typeof formatted.features === 'string') {
        formatted.features = formatted.features.split(',').map(s => s.trim()).filter(Boolean);
      } else if (!formatted.features) {
        formatted.features = [];
      }

      // Fallback description if full details are empty
      if (formatted.shortDescription && !formatted.description) {
        formatted.description = formatted.shortDescription;
      }
      
      return formatted;
    });
    
    // Ensure data dir exists
    const dataDir = path.dirname(outputFile);
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true });
    }
    
    // Save to file
    fs.writeFileSync(outputFile, JSON.stringify(finalData, null, 2));
    console.log(`Saved ${finalData.length} entries to ${outputFile}`);
    
  } catch (err) {
    console.error(`Error fetching/parsing data:`, err);
    process.exit(1);
  }
}

async function main() {
  const toolsMap = {
    'Name': 'name',
    'Slug': 'slug',
    'Short Description': 'shortDescription',
    'Full Details': 'description',
    'Category': 'category',
    'Pricing': 'pricing',
    'URL': 'website',
    'Logo URL': 'logo',
    'Tags': 'tags',
    'Features': 'features',
    'Date Added': 'dateAdded'
  };
  
  const ideasMap = {
    'Title': 'title',
    'Slug': 'slug',
    'Summary': 'summary',
    'Difficulty': 'difficulty',
    'Category': 'category'
  };

  await fetchAndSave(TOOLS_URL, toolsMap, path.join(process.cwd(), 'data', 'tools.json'));
  await fetchAndSave(IDEAS_URL, ideasMap, path.join(process.cwd(), 'data', 'ideas.json'));
}

main();
