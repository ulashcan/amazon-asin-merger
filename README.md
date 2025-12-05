# Amazon ASIN Merger

A small Python script I wrote to collect unique ASIN values from multiple CSV files.

### How it works
- Scans all `.csv` files in the given folder
- Reads the `ASIN` column
- Stores each ASIN only once
- Writes them into output text files in batches of 3000

This was one of my early utilities for working with Amazon data. 
