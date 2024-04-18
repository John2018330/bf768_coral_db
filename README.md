links to include in help pages or other places  https://bumarine.smugmug.com/ORGANISMS/METAZOA-animals/CNIDARIA


Graph: 
        location vs counts of mean ln_volume


        line graph ln_volume over the years for one 

        
        counts of variant by location



To do before presentation on 25th:
- Home page: 
*  [] Need to make it prettier 
*  [] Add more context on data/project
- Data page:
*  [] Need to include group by/aggregate functions
*  [] Screenshots of resultant tables post filtering
*  [] Screenshots of graph (need to add charts, variable columns for plotting, etc)
*  [] Need to add: Linked sample data or javascript filling of forms (where necessary) for trying out database features anywhere data input is required.
- Media page:
*  [] Need to link to external database (coral pics)
*  [] Talk to Benson about what is expected
- Help page:
*  [] Need to add more context for all tabs (length/width/height)
*  [] Search tab?
*  [] Links from your HTML forms explaining what the page does (Ask Benson)
*  [] Add the format of input (Ask Benson)

Done:
- [x] Separate Introduction HTML page
- [ ] Data Download (maybe ajax?)


UI to implement for phenotypic data
'WHERE' might be implemented by having a number of checkbox options for what to filter by, same with group by
- [ ] Slider for important numeric column like eco volume (query = WHERE X > Y) 
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


