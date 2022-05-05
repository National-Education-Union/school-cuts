# School cuts map
The school funding information can be found on a map at [www.schoolcuts.org.uk](www.schoolcuts.org.uk).

# Findings
We found that out of the 20,319 schools with comparable data 14,227 (70%) had less spending power in 2020-21 compared with 2015-16. This is despite the fact that in 2020-21 schools had additional funding to spend on mitigating the spread coronavris and funding to support pupils catching-up their lost learning.

Per pupil funding felll by -£362 on average from £6,837 in 2015-16 to £6,475 in 2020-21 (in 2022-23 prices). This cut in per pupil funding is equivalent to a cut in school spending power of -£2.8 bn or 6%.

These funding cuts were not evenly spread. 

These cuts varied by school type with mainstream primary schools least affected and nursery schools, all-through schools and special schools worst affected.

![image](https://user-images.githubusercontent.com/4374366/167014371-6d6f8a84-6beb-4f22-9280-d350e8d44edd.png)

In addition, schools with greater levels of poverty amongst their pupils harder hit than schools serving the less disadvantaged.

![image](https://user-images.githubusercontent.com/4374366/167015538-034aedf3-8f58-4861-8b79-70c75262bbab.png)

There was also signficant regional and local variation.

![image](https://user-images.githubusercontent.com/4374366/167016048-8d945b8b-1406-4a08-9c83-f270c8cf6464.png)

The twenty worst hit local authorities were:

![image](https://user-images.githubusercontent.com/4374366/167016757-df54d188-4f07-4c1d-a238-3dd92728ea47.png)

It is striking that despite the claimed ambition of the Government to address histroic under-funding, only 7 out of 152 local authorities saw an increase in their spending power:

![image](https://user-images.githubusercontent.com/4374366/167017084-ba5b3359-6db4-40a9-bb0b-fc2da0a7f71a.png)

The summary tabels are contained in the [output folder](https://github.com/National-Education-Union/school_cuts/tree/main/output).


# School cuts methodology

## School funding
We took the grant funding for every school in 2015-16 and compared it with 2020-21.
Grant funding is all the revenue funding the Government allocates to schools. It includes:
- Funding for 2- to 16-year-olds (I01),
- Special needs funding (I02),
- Sixth-form funding (I03),
- Pupil Premium (I04),
- Funding for pupils with Education and Health Care Plans (I05),
- Funding for minority ethnic pupils (I06),
- Other grants such as the milk subsidy (I07),
- Funding for extended schools (I15),
- Funding to be attributed to community-focused activities (I16), and
- Additional grants for schools such as the primary PE and sports grant and universal infant free school meal funding (I18). For 2020-21, this also includes funding for coronavirus mtigation and catch-up funding for pupils.

The source for this data is from the [Schools financial benchmarking](https://schools-financial-benchmarking.service.gov.uk/Help/DataSources) and the full description of the funding elements is described in the [Consistent financial reporting framework](https://www.gov.uk/guidance/consistent-financial-reporting-framework-2020-to-2021/income).

## School costs index
We have updated and extended the index of school costs published by the National Audit Office in their report, ["Financial sustainability of schools"](https://www.nao.org.uk/wp-content/uploads/2016/12/Financial-sustainability-of-schools.pdf).

![image](https://user-images.githubusercontent.com/4374366/166971613-2750e6d7-b8d4-4ca9-aa86-2e78f930816e.png)

This chart shows cumulative costs pressures facing schools, 2016-17 to 2019-20

We have used these figures for additional National Insurance costs and the Teachers’ Pension Scheme. We have used the Department for Education (DfE) documents:
- [Schools’ costs: 2018 to 2019 and 2019 to 2020 (Feb 2018)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/678439/Schools_costs_technical_note.pdf)
- [Schools’ costs: 2018 to 2019 and 2019 to 2020 (Jan 2019)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/774325/Schools_costs_technical_note_Jan_2019.pdf)
- [Schools’ costs: 2020 to 2021 (Jan 2021)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/961096/Schools_costs_technical_note_January_2021.pdf)

### Non-staff costs
We have updated non-staff costs with the latest estimates for the GDP deflator measure of inflation from HM Teasury, [GDP deflators at market prices, and money GDP March 2022 (Spring Statement)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1062965/GDP_Deflators_Spring_Statement_March_2022_update.xlsx).

### Support staff pay
The DfE documents uses the National Joint Council (NJC) pay awards, which cover all local authority staff. However, school support staff are paid signifcantly less well paid than council staff and many are employed on the minimum wage. In recent years, there have been significant uplifts in the minimum wage. We made an index for school support staff pay by sending Freedom of Information requests to a sample of local authorities and then tracked the value of those pay points back to 2009-10 and weighted them by the number of staff paid on each grade from the FOIs. The increases in the minimum wage have had a substantial impact on school support staff pay and their pay has risen much faster than the headline rates for the NJC awards.

![image](https://user-images.githubusercontent.com/4374366/166963983-2fe4ca2f-c4c2-4cd9-9e69-f05601edd747.png)

## School costs index

![image](https://user-images.githubusercontent.com/4374366/166983069-2d86ff8f-9602-4c11-bc53-f6bc76eb9e0a.png)

The calculations be found in the spreadsheet, [school costs.xlsx](https://github.com/National-Education-Union/school_cuts/blob/main/data/school_costs/school%20costs.xlsx).

## Calculating school funding changes
For each school we calculated the Grant Funding (2022-23 prices) by multiplying it by the school costs index. 
We calculated the per pupil funding by diving it by the number of pupils reported in the school funding tables. 
To calculate the change in spending power, we found the difference in the real-terms per pupil funding between 2015-16 and 2020-21 and then multiplying it by the number of pupils in 2020-21.

To calculate the aggregate funding changes by local authority, trust, parliamentary constituency and district; we calculated the change in real-terms per pupil funding by summing all the Grant Funding in 2022-23 prices for schools where funding data was available for both 2015-16 and 2022-23 and then divided it by the total number of pupils in those schools. We then made the spending power calculation as above.

### Anomalies
We found some anomolies in the data. The number of pupils in Alternative Provision and Pupil Referal Units was wrong for 2016-17 and so we excluded them. 
We also found that some schools had clearly misreported their funding or pupils numbers, so we excluded all schools with a change in funding up or down of greater than 50%. 

## Code
These calculations are contained in the Python script, [school_cuts.py](school_cuts.py).
[edubase.py](edubase.py) downloads the latest version of school information from [Get Information About Schools](https://get-information-schools.service.gov.uk/Downloads). 
[school_cuts.py](school_cuts.py) uses this information to update the Unique Reference Number for schools that have converted to academy status, calculates the changes in school funding and produces summary tables.
The Excel file with information for all schools and the summary tabels are contained in the [output folder](https://github.com/National-Education-Union/school_cuts/tree/main/output).
