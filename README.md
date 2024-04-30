links to include in help pages or other places  https://bumarine.smugmug.com/ORGANISMS/METAZOA-animals/CNIDARIA


Graph: 
        location vs counts of mean ln_volume


        line graph ln_volume over the years for one 

        
        counts of variant by location

## To do before demonstration on 8th:

### !! IMPORTANT !!

Data page:
*  [ ] Download table data (Saumya)
*  [ ] Group by working (John)
*  [ ] Throw an error if no year is selected + if both tagid and scaffold ids have values (Zach)

List of CGI forms (queries):

*  [ ] Get VCF individuals (from 2018) that are alive
*  [ ] Select average length by location in 2015
*  [ ] GRAPH QUERY: get SNP's counts by location 
*  [ ] GRAPH QUERY: Group by location and find ecological volume
*  [ ] GRAPH QUERY: Group by location Volume over 4 years
*  [ ] Get counts of alive and dead by  location
*  [ ] UPDATE [table] SET [column]= "-" WHERE [column] IS NULL

Help Page:
*  [ ] Explanation on reset buttons. (Saumya)
*  [ ] Add that phenotypic data repeats (in a div tag) (Saumya)
*  [ ] Add info on graph tab + links (Saumya)

## Done:

General:
*  [x] Separate Introduction HTML page

Home Page:
*  [x] Need to make it prettier 
*  [x] Add more context on data/project

Data Page:
*  [x] Click on eg to fill in text box (javascript filling of forms).
*  [x] Add a reset button for the sliders + reset all which resets ALL filters.
*  [x] Shift sliders to the right if possible? 2 side by side (Not possible)
*  [x] Help link doesn't work for sliders.
*  [x] Relative scrolling for table output.
*  [x] Add advanced filter column which allows GROUP BY (for aggregate functions).
*  [x] Link to vcf checkbox (True/False?)
*  [x] Make count and average of advanced filters a drop down menu
*  [x] Fix allele frequency slider (Saumya)
*  [x] Google charts (Add line chart)

Media Page:
*  [x] Need to link to external database (coral pics)
*  [x] Add links for different corals + different directories + whole website. (use href)
*  [x] Fix tooltip position issue due to scrolling
*  [x] Fix href header being blue/purple

Help Page:
*  [x] Need to add more context for all tabs (length/width/height)
*  [x] Links from your HTML forms explaining what the page does
*  [x] Add the format of input (Note: exact format not needed. Add links to help page and maybe images of the slider being used).

UI to implement for phenotypic data:
'WHERE' might be implemented by having a number of checkbox options for what to filter by, same with group by
*  [x] Slider for important numeric column like eco volume (query = WHERE X > Y) 
*  [x] Group by Location
*  [x] Checkboxes for year
*  [x] Filter by alive or dead
*  [x] Auxillary If group by, offer additional filters (having x > y)
*  [x] Auxillary Provide option for performing aggregate functions
*  [x] Filter the VCF by quality (Not needed)

UI to implement for VCF:
- [x] Slider for allele frequency
- [x] Slider for quality filtering maybe (Not Needed)
- [x] Textbox for scaffold and maybe position (it's possible multiple SNP's exist per scaffold)

## John To Do
- [ ] Dropdown Menu for scaffold
