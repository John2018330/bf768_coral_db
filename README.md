links to include in help pages or other places  https://bumarine.smugmug.com/ORGANISMS/METAZOA-animals/CNIDARIA


Graph: 
        location vs counts of mean ln_volume


        line graph ln_volume over the years for one 

        
        counts of variant by location



To do before presentation on 25th:

Home page: (priority = 4)
*  [ ] Need to make it prettier 
*  [ ] Add more context on data/project

Data page: (priority = 1)
*  [ ] Screenshots of resultant tables post filtering
*  [ ] Screenshots of graph (need to add charts, variable columns for plotting, etc)
*  [ ] Add a reset button for the sliders + reset all which resets ALL filters.
*  [ ] Shift sliders to the right if possible? 2 side by side
*  [ ] Click on eg to fill in text box (javascript filling of forms).
*  [x] Relative scrolling for table output.
*  [x] Add advanced filter column which allows GROUP BY (for aggregate functions).
*  [x] Link to vcf checkbox (True/False?)

Media page: (priority = 3)
*  [ ] Need to link to external database (coral pics)
*  [ ] Add links for different corals + different directories + whole website. (use href)

Help page: (priority = 2)
*  [x] Need to add more context for all tabs (length/width/height)
*  [ ] Search button?
*  [ ] Links from your HTML forms explaining what the page does
*  [ ] Add the format of input (Note: exact format not needed. Add links to help page and maybe images of the slider being used)

Done:
- [x] Separate Introduction HTML page
- [ ] Data Download (maybe ajax?)


UI to implement for phenotypic data
'WHERE' might be implemented by having a number of checkbox options for what to filter by, same with group by
- [x] Slider for important numeric column like eco volume (query = WHERE X > Y) 
- [ ] Group by Location
- [x] Checkboxes for year
- [x] Filter by alive or dead
- [ ] Auxillary If group by, offer additional filters (having x > y)
- [ ] Auxillary Provide option for performing aggregate functions

UI to implement for VCF
- [x] Slider for allele frequency
- [x] Slider for quality filtering maybe (Not Needed)
- [x] Textbox for scaffold and maybe position (it's possible multiple SNP's exist per scaffold)
- [ ] Ajax for textbox? (Suggestions based on ID/Scaffold entered?)


List of CGI forms (queries)
- [x] Filter the VCF by quality (Not needed)
- [ ] Get VCF individuals (from 2018) that are alive
- [ ] Select average length by location in 2015
- [ ] GRAPH QUERY: get SNP's counts by location 
- [ ] GRAPH QUERY: Group by location and find ecological volume
- [ ] GRAPH QUERY: Group by location Volume over 4 years
- [ ] Get counts of alive and dead by location
- [ ] 

John To Do
- [ ] Dropdown Menu for scaffold


