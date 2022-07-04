# School cuts map
The school funding information for every school can be found on a map at [www.schoolcuts.org.uk](www.schoolcuts.org.uk).

# Findings
We found that out of the 20,319 schools with comparable data 14,227 (70%) had less spending power in 2020-21 compared with 2015-16. This is despite the fact that in 2020-21 schools had additional funding to spend on mitigating the spread coronavirus and funding to help pupils catch-up on their lost learning.

Real terms per pupil funding was cut by £362 on average from £6,837 in 2015-16 to £6,475 in 2020-21 (in 2022-23 prices). This cut in per pupil funding is equivalent to a cut in school spending power of £2.8 bn or 6%.

These funding cuts were not evenly spread. 

These cuts varied by school type with mainstream primary schools least affected and nursery schools and special schools worst affected.
<img src="https://user-images.githubusercontent.com/4374366/177146375-d3dffff3-b94e-4af7-a71f-efe3361a6f8a.png" width="600">

In addition, schools with greater levels of poverty amongst their pupils were harder hit than schools serving the less disadvantaged.

<img src="https://user-images.githubusercontent.com/4374366/177146437-ba777f7d-bf50-4705-9979-492da1ca996b.png" width="600">

<img src="https://user-images.githubusercontent.com/4374366/177146497-2322a2d4-7bd3-4086-808a-3210e6ee26de.png" width="600">

There was also significant regional and local variation.

<img src="https://user-images.githubusercontent.com/4374366/177146559-73778363-f4e2-4877-86a0-9ae810248b6d.png" width="600">

The twenty worst hit local authorities were:

![image](https://user-images.githubusercontent.com/4374366/177141514-6db07134-b964-4180-8f54-4741d8222c6d.png)

It is striking that despite the claimed ambition of the Government to address historic under-funding, only 22 out of 152 local authorities saw an increase in their spending power:

![image](https://user-images.githubusercontent.com/4374366/177141790-40d8b4fd-0139-4999-b68f-6944971c9881.png)

The summary tables are contained in the [output folder](https://github.com/National-Education-Union/school_cuts/tree/main/output).


# Methodology

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
- Additional grants for schools such as the primary PE and sports grant and universal infant free school meal funding (I18). For 2020-21, this also includes funding for coronavirus mitigation and catch-up funding for pupils.

This data was taken from [Schools financial benchmarking](https://schools-financial-benchmarking.service.gov.uk/Help/DataSources) and the full description of the funding elements is described in the [Consistent financial reporting framework](https://www.gov.uk/guidance/consistent-financial-reporting-framework-2020-to-2021/income).

## School costs index
We have updated and extended the index of school costs published by the National Audit Office in their report, ["Financial sustainability of schools"](https://www.nao.org.uk/wp-content/uploads/2016/12/Financial-sustainability-of-schools.pdf).

This chart shows cumulative costs pressures facing schools, 2016-17 to 2019-20
<img src="https://user-images.githubusercontent.com/4374366/177144873-eb516580-7eb4-4a94-851c-b9a3b98452a9.png" width="500">

We have used these figures for additional National Insurance costs and the Teachers’ Pension Scheme. We have used the Department for Education (DfE) documents:
- [Schools’ costs: 2018 to 2019 and 2019 to 2020 (Feb 2018)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/678439/Schools_costs_technical_note.pdf)
- [Schools’ costs: 2018 to 2019 and 2019 to 2020 (Jan 2019)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/774325/Schools_costs_technical_note_Jan_2019.pdf)
- [Schools’ costs: 2020 to 2021 (Jan 2021)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/961096/Schools_costs_technical_note_January_2021.pdf)

### Non-staff costs
We have updated non-staff costs with the latest estimates for the GDP deflator measure of inflation from HM Treasury, [GDP deflators at market prices, and money GDP March 2022 (Spring Statement)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1062965/GDP_Deflators_Spring_Statement_March_2022_update.xlsx).

### Support staff pay
The DfE documents uses the National Joint Council (NJC) pay awards, which cover all local authority staff, the DfE adjusted the award for increases in the National Living Wage. In recent years, there have been uplifts in the minimum wage that outstrip pay awards for other council workers. We made an index for school support staff pay by sending Freedom of Information requests (FOIs) to a sample of local authorities and then tracked the value of the pay points back to April 2015 and weighted them by the number of staff paid on each grade from the FOIs. 

![image](https://user-images.githubusercontent.com/4374366/177144593-f423b80a-3fa7-41fd-8498-07ae766f8ab7.png)

Our results concur with the DfE analysis for the period 2018 to 2020, where they have estimated the increase in pay as 6.3% over the two years. We disagree with the DfE estimate for 2019 to 2020. The DfE gave the figure for 2.4%; however, the NJC award was 2.75% on all grades. The spreadsheet with the calculations are in [school support staff pay.xlsx](https://github.com/National-Education-Union/school_cuts/blob/main/data/school_costs/school%20support%20staff%20pay.xlsx).

## School costs index

<img src="https://user-images.githubusercontent.com/4374366/177145549-893b03dc-01ff-402c-96f0-0ce35181b936.png" width="500">

The calculations be found in the spreadsheet, [school costs.xlsx](https://github.com/National-Education-Union/school_cuts/blob/main/data/school_costs/school%20costs.xlsx).

## Calculating school funding changes
For each school we calculated funding in 2022-23 prices using the school costs index. 
We calculated the per pupil funding by diving it by the number of pupils reported in the school funding tables. 
To calculate the change in spending power, we found the difference in the real terms per pupil funding between 2015-16 and 2020-21 and then multiplying it by the number of pupils in 2020-21.

To calculate the aggregate funding changes by local authority, trust, parliamentary constituency and district; we calculated the change in real terms per pupil funding by summing all the Grant Funding in 2022-23 prices for schools where funding data was available for both 2015-16 and 2022-23 and then divided it by the total number of pupils in those schools. We then made the spending power calculation as above.

![image](https://user-images.githubusercontent.com/4374366/167357380-ec16e402-d01f-425f-85c7-1255aeeb2244.png)

For the summary tables looking at the deprivation of pupils, we grouped schools by phase and then split them into quintiles using the proportion of pupils receiving free school meals. 

### Anomalies
We found some anomalies in the data. The number of pupils in Alternative Provision and Pupil Referral Units was wrong for 2016-17 and so we excluded them. 
We also found that some schools had clearly misreported their funding or pupil numbers, so we excluded all schools with a change in funding up or down of greater than 50%. 

## Code
The funding calculations are contained in the Python script, [school_cuts.py](school_cuts.py).

[edubase.py](edubase.py) downloads the latest version of school information from [Get Information About Schools](https://get-information-schools.service.gov.uk/Downloads) and uses this to update the Unique Reference Number for schools so they can be compared over time.

An Excel file with information for all schools and the summary tables are contained in the [output folder](https://github.com/National-Education-Union/school_cuts/tree/main/output).
