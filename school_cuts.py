from pandas import read_excel, concat, Series, qcut, MultiIndex, ExcelWriter
from numpy import nan
from edubase import update_urn, edubase

output_dir = 'output/'

years = ['2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21']
school_costs = {
    '2015-16' : 0.793060264868583,
    '2016-17' : 0.817400825132381,
    '2017-18' : 0.835278397499553,
    '2018-19' : 0.85607220163531,
    '2019-20' : 0.897227197542682,
    '2020-21' : 0.929419593059095,
    '2021-22' : 0.943229894944067,
    '2022-23' : 1,
    }

maintained_2015_16 = read_excel(
    'data/cfr/School_Total_Spend_2015-16_Full_Data_Workbook.xlsx',
    skiprows=3,
    sheet_name='Raw CFR Data',
    usecols=[0, 15, 19, 20, 21, 22, 23, 24, 25, 32, 33, 35],
    index_col=0,
    names=['URN', 'Pupils', 'I01', 'I02', 'I03', 'I04',
       'I05', 'I06', 'I07', 'I15', 'I16', 'I18'],
    na_values=['SUPP'],
    ).dropna()
maintained_2015_16['Grant Funding'] = (
    maintained_2015_16.I01 +
    maintained_2015_16.I02 +
    maintained_2015_16.I03 +
    maintained_2015_16.I04 +
    maintained_2015_16.I05 +
    maintained_2015_16.I06 +
    maintained_2015_16.I07 +
    maintained_2015_16.I15 +
    maintained_2015_16.I16 +
    maintained_2015_16.I18
    )
maintained_2015_16.drop(
    columns=[
        'I01', 'I02', 'I03', 'I04', 'I05', 'I06', 'I07', 'I15', 'I16', 'I18'
        ],
    inplace=True
    )
academies_2015_16 = concat(               
    [
        read_excel(
            'data/cfr/SFR32_2017_Main_Tables.xlsx',
            skiprows=4,
            sheet_name='Raw Data SATs',
            usecols=[5, 6, 24],
            index_col=0,
            names=['URN', 'Pupils', 'Grant Funding'],
            na_values=['SUPP', 'NS'],
            ).dropna(),
        read_excel(
            'data/cfr/SFR32_2017_Main_Tables.xlsx',
            skiprows=4,
            sheet_name='Raw Data MATs',
            usecols=[7, 8, 26],
            index_col=0,
            names=['URN', 'Pupils', 'Grant Funding'],
            na_values=['SUPP', 'NS'],
            ).dropna(),
        ]
    )
academies_2015_16['Grant Funding'] *= 1000
print('Imported data for 2015-16')

csvs = {
       '2015-16': concat([maintained_2015_16, academies_2015_16]),
       '2016-17': concat(
           [
               read_excel(
                   'data/cfr/School_total_spend_2016-17_Full_Data_Workbook.xlsx',
                   skiprows=0,
                   sheet_name='Maintained',
                   usecols=[3, 8, 80],
                   index_col=0,
                   names=['URN', 'Pupils', 'Grant Funding'],
                   na_values=['SUPP', 'NS'],
                   ).dropna(),
               read_excel(
                   'data/cfr/SFB_Academies_2016-17_download.xlsx',
                   sheet_name='Academies 2016 to 17',
                   skiprows=2,
                   usecols=[3, 16, 87],
                   index_col=0,
                   names=['URN', 'Pupils', 'Grant Funding'],
                   na_values=['SUPP', 'NS'],
                   ).dropna(),
               ]
           ),
       '2017-18': concat(
           [
               read_excel(
                   'data/cfr/School_total_spend_2017-18_Full_Data_Workbook.xlsx',
                   sheet_name='Raw CFR Data',
                   skiprows=3,
                   usecols=[6, 13, 103],
                   index_col=0,
                   names=['URN', 'Pupils', 'Grant Funding'],
                   na_values=['SUPP', 'NS'],
                   ).dropna(),
               read_excel(
                   'data/cfr/SFB_Academies_2017-18_download.xlsx',
                   sheet_name='Academies 2017 to 18',
                   skiprows=2,
                   usecols=[3, 15, 83],
                   index_col=0,
                   names=['URN', 'Pupils', 'Grant Funding'],
                   na_values=['SUPP', 'NS'],
                   ).dropna(),
               ]
           ),
       '2018-19': concat(
           [
               read_excel(
                   'data/cfr/School_total_spend_2018-19_Full_Data_Workbook.xlsx',
                   sheet_name='CFR Data',
                   skiprows=2,
                   usecols=[6, 13, 105],
                   index_col=0,
                   names=['URN', 'Pupils', 'Grant Funding'],
                   na_values=['SUPP', 'NS'],
                   ).dropna(),
               read_excel(
                   'data/cfr/SFB_Academies_2018-19_download.xlsx',
                   sheet_name='Academies 2018 to 19',
                   skiprows=2,
                   usecols=[3, 16, 84],
                   index_col=0,
                   names=['URN', 'Pupils', 'Grant Funding'],
                   na_values=['SUPP', 'NS'],
                   ).dropna(),
               ]
           ),
       '2019-20': concat(
           [
               read_excel(
                   'data/cfr/School_total_spend_2019-20_Full_Data_Workbook.xlsx',
                   sheet_name='CFR Data',
                   skiprows=3,
                   usecols=[6, 13, 100],
                   index_col=0,
                   names=['URN', 'Pupils', 'Grant Funding'],
                   na_values=['SUPP', 'NS'],
                   ).dropna(),
               read_excel(
                   'data/cfr/SFB_Academies_2019-20_download.xlsx',
                   sheet_name='Academies',
                   skiprows=2,
                   usecols=[3, 16, 86],
                   index_col=0,
                   names=['URN', 'Pupils', 'Grant Funding'],
                   na_values=['SUPP', 'NS', '        NA'],
                   ).dropna(),
               ]
           ),
       '2020-21': concat(
           [
               read_excel(
                   'data/cfr/School_total_spend_2020-21_Full_Data_Workbook.xlsx',
                   sheet_name='CFR_Output',
                   skiprows=2,
                   usecols=[6, 9, 13, 86],
                   index_col=0,
                   names=['URN', 'Phase', 'Pupils', 'Grant Funding'],
                   na_values=['SUPP', 'NS'],
                   ).dropna(),
               read_excel(
                   'data/cfr/SFB_Academies_2020-21_download.xlsx',
                   sheet_name='Academies',
                   skiprows=2,
                   usecols=[3, 16, 19, 85],
                   index_col=0,
                   names=['URN', 'Pupils', 'Phase', 'Grant Funding'],
                   na_values=['SUPP', 'NS', 'DNS'],
                   ).dropna(),
               ]
           ),
       }
print('Imported data for 2017-21')

for year in years:
    csvs[year] = csvs[year].loc[
        (csvs[year]['Pupils']!=0) & (csvs[year]['Grant Funding']!=0)
        ].copy()
    csvs[year] = update_urn(csvs[year])
    print(f'URNs updated for {year}')

funding = concat(csvs, names=['Year'])
funding = funding.reorder_levels(['URN', 'Year'])
funding = funding.unstack()
funding.drop(
    columns=[
        ('Phase', '2015-16'),
        ('Phase', '2016-17'),
        ('Phase', '2017-18'),
        ('Phase', '2018-19'),
        ('Phase', '2019-20'),
        ],
    inplace=True
    )
funding = funding[
    [funding.columns[-1]] + funding.columns[:-1].tolist()
    ].copy()
for year in years:
    funding[('Grant Funding (2022-23 prices)'), year] = (
        funding[('Grant Funding', year)] /
        school_costs[year]
        )
for year in years:
    funding[('Grant Funding Per Pupil (2022-23 prices)', year)] = (
        funding[('Grant Funding (2022-23 prices)', year)] /
        funding[('Pupils', year)]
        )
for year in years[1:]:
    funding[('Change in spending power with 2015-16', year)] = (
        (
            funding[('Grant Funding Per Pupil (2022-23 prices)'), year] - 
            funding[('Grant Funding Per Pupil (2022-23 prices)'), '2015-16']
            ) *
        funding[('Pupils', year)]
        )
for year in years[1:]:
    funding[('Change in spending power with 2015-16 (%)', year)] = (
        funding[('Grant Funding Per Pupil (2022-23 prices)'), year] /
        funding[('Grant Funding Per Pupil (2022-23 prices)'), '2015-16'] - 1
        )
print('Grant funding per pupil calculated')

# AP & PRU pupil numbers wrong for 2016-17
funding.loc[
    (funding[('Phase', '2020-21')]=='Alternative provision') |
    (funding[('Phase', '2020-21')]=='Pupil referral unit'),
    ('Pupils', '2016-17')
    ] = nan
funding.loc[
    (funding[('Phase', '2020-21')]=='Alternative provision') |
    (funding[('Phase', '2020-21')]=='Pupil referral unit'),
    ('Change in spending power with 2015-16 (%)', '2016-17')
    ] = nan
funding.loc[
    (funding[('Phase', '2020-21')]=='Alternative provision') |
    (funding[('Phase', '2020-21')]=='Pupil referral unit'),
    ('Change in spending power with 2015-16', '2016-17')
    ] = nan
# remove schools with anomalous funding change

for year in years[1:]:
    funding.loc[
        (funding[('Change in spending power with 2015-16 (%)', year)]>.5) |
        (funding[('Change in spending power with 2015-16 (%)', year)]<-.5),
        ('Change in spending power with 2015-16 (%)', year)
        ] = nan
    funding.loc[
        (funding[('Change in spending power with 2015-16 (%)', year)]>.5) |
        (funding[('Change in spending power with 2015-16 (%)', year)]<-.5),
        ('Change in spending power with 2015-16', year)
        ] = nan
for year in years[1:]:
    funding.loc[
        funding[('Change in spending power with 2015-16 (%)', year)]<0,
        ('Schools with cut in spending power', year)
        ] = 1
    funding.loc[
        funding[('Change in spending power with 2015-16 (%)', year)]>=0,
        ('Schools with cut in spending power', year)
        ] = 0
print('Removed schools with anomalous funding change')

edu = edubase[
    [
        'EstablishmentName',
        'EstablishmentNumber', 
        'LA (code)',
        'LA (name)',
        'Trusts (code)',
        'Trusts (name)',
        'GOR (code)',
        'GOR (name)',
        'DistrictAdministrative (code)',
        'DistrictAdministrative (name)',
        'ParliamentaryConstituency (code)',
        'ParliamentaryConstituency (name)',
        'PercentageFSM',
        ]
    ].copy()
edu.loc[
        (edu.EstablishmentNumber.notnull()) &
        (edu['LA (code)'].notnull()),
        'LAESTAB'
        ] = edu['LA (code)']*10000 + edu.EstablishmentNumber
edu = edu[
    [
        'LAESTAB',
        'EstablishmentName',
        'LA (code)',
        'LA (name)',
        'Trusts (code)',
        'Trusts (name)',
        'GOR (code)',
        'GOR (name)',
        'DistrictAdministrative (code)',
        'DistrictAdministrative (name)',
        'ParliamentaryConstituency (code)',
        'ParliamentaryConstituency (name)',
        'PercentageFSM',
        ]
    ].copy()
edu.columns = MultiIndex.from_tuples([(col, '') for col in edu.columns])
funding = edu.merge(
        funding,
        how='right',
        left_index=True,
        right_index=True,
        )
print('Added demographic data for schools')

band_map = {
    4: {0: '1. Least', 1: '2. Low', 2: '3. Average', 3: '4. High', 4: '5. Highest'},
    3: {0: '1. Least', 1: '2. Low', 2: '4. High', 3: '5. Highest'},
    2: {0: '2. Low', 1: '3. Average', 2: '4. High'},
    1: {0: '2. Low', 1: '4. High'},
    0: {0: '3. Average'},
    }
fsm_band_mapper = lambda x: Series(
    qcut(
        x,
        5,
        labels=False,
        duplicates='drop'
        ),
    index=x.index
    )
funding['Free School Meals band'] = funding.groupby(
    ('Phase', '2020-21')
    )['PercentageFSM'].apply(fsm_band_mapper)
phases = sorted(
    [p for p in funding['Phase', '2020-21'].unique() if type(p)==str]
    )
for phase in phases:
    bands = funding.loc[
        (funding[('Phase', '2020-21')]==phase) &
        (funding[('Free School Meals band', '')].notnull())
        ][('Free School Meals band', '')].max()
    funding.loc[
        funding[('Phase', '2020-21')]==phase, 
        'Free School Meals band'
        ] = funding.loc[
            funding[('Phase', '2020-21')]==phase
            ][('Free School Meals band', '')].map(band_map[bands]).tolist()
funding = funding[
    funding.columns[:13].tolist() + 
    [funding.columns[-1]] + 
    funding.columns[13:-1].tolist()
    ].copy()
print('Schools FSM quintiles calculated')

groups = [
    {
        'groupby': [
            ('Phase', '2020-21'), ('Free School Meals band', '')
            ],
        'filename': 'Phase & Deprivation',
        'make_charts': False,
        },
    {
        'groupby':[('Phase', '2020-21')],
        'filename': 'Phase',
        'make_charts': False,
        },
    {
        'groupby': [('Free School Meals band', '')],
        'filename': 'Deprivation',
        'make_charts': False,
        },
    {
        'groupby': [('GOR (name)', ''), ('Free School Meals band', '')],
        'filename': 'Region & Deprivation',
        'make_charts': False,
        },
    {
        'groupby': [('GOR (name)', ''), ('Phase', '2020-21')],
        'filename': 'Region & Phase',
        'make_charts': False,
        },
    {
        'groupby': [
            ('GOR (name)', ''),
            ('Phase', '2020-21'),
            ('Free School Meals band', '')
            ],
        'filename': 'Region, Phase & Deprivation',
        'make_charts': False,
        },
    {
        'groupby': ('GOR (name)', ''),
        'filename': 'Region',
        'make_charts': False,
        },
    ]

essential_columns = [('Free School Meals band', ''), ('Phase', '2020-21')]
for year in years[1:]:
    essential_columns.append(('Change in spending power with 2015-16 (%)', year))
    essential_columns.append(('Change in spending power with 2015-16', year))
funding_out = funding.dropna(subset=essential_columns)
funding.to_csv('csv/funding.csv')
print('Funding CSV exported')

agg = {
       ('EstablishmentName', ''): 'count',
       }
for year in years:
    agg[('Pupils', year)] = 'sum'
for year in years:
    agg[('Grant Funding (2022-23 prices)', year)] = 'sum'
for year in years[1:]:
    agg[('Schools with cut in spending power', year)] = 'mean'

for group in groups:
    summary = funding_out.groupby(group['groupby']).agg(agg)
    summary.rename(
        columns={'EstablishmentName': 'Schools'},
        inplace=True
        )
    for year in years:
        summary[('Grant Funding Per Pupil (2022-23 prices)', year)] = (
            summary[('Grant Funding (2022-23 prices)', year)] /
            summary[('Pupils', year)]
            )
    for year in years[1:]:
        summary[('Change in per pupil funding with 2015-16', year)] = (
            summary[('Grant Funding Per Pupil (2022-23 prices)'), year] -
            summary[('Grant Funding Per Pupil (2022-23 prices)'), '2015-16']
            )
    for year in years[1:]:
        summary[('Change in spending power with 2015-16 (%)', year)] = (
            summary[('Grant Funding Per Pupil (2022-23 prices)'), year] /
            summary[('Grant Funding Per Pupil (2022-23 prices)'), '2015-16'] - 1
            )
    summary.index.names = [ind[0] for ind in summary.index.names]
    writer = ExcelWriter(
        f"{output_dir}/{group['filename']}.xlsx",
        engine='xlsxwriter',
    )
    summary.to_excel(writer, 'Data')
    worksheet = writer.sheets['Data']
    workbook = writer.book
    index_format = workbook.add_format()
    index_format.set_align('top')
    index_format.set_align('left')
    index_format.set_bold()
    index_format.set_border()
    percent= workbook.add_format()
    percent.set_num_format('0%')
    gbp = workbook.add_format()
    gbp.set_num_format('"£"#,##0')
    gbp_m = workbook.add_format()
    gbp_m.set_num_format('"£"0.0,," mn";-"£"0.0,," mn"')
    int_format = workbook.add_format()
    int_format.set_num_format('#,##0')
    col_offset = len(summary.index.names)-1
    worksheet.set_column(0, col_offset, 20, index_format)
    worksheet.set_column(col_offset+1, col_offset+7, 10, int_format)
    worksheet.set_column(col_offset+8, col_offset+13, 10, gbp_m)
    worksheet.set_column(col_offset+14, col_offset+18, 10, percent)
    worksheet.set_column(col_offset+19, col_offset+29, 10, gbp)
    worksheet.set_column(col_offset+30, col_offset+34, 10, percent)
    worksheet.freeze_panes(3, col_offset+1)
    writer.close()


groups = [
    {
        'groupby': [
            ('DistrictAdministrative (name)', ''),
            ('DistrictAdministrative (code)', ''),
            ],
        'filename': 'District',
        'make_charts': False,
        },
    {
        'groupby':[('Trusts (name)', ''), ('Trusts (code)', '')],
        'filename': 'Multi Academy Trusts',
        'make_charts': False,
        },
    {
        'groupby': [('LA (name)', ''), ('Phase', '2020-21')],
        'filename': 'Local Authority & Phase',
        'make_charts': False,
        },
    {
        'groupby':[('LA (name)', ''), ('LA (code)', '')],
        'filename': 'Local Authority',
        'make_charts': False,
        },
    {
        'groupby':[
        ('ParliamentaryConstituency (name)', ''),
        ('ParliamentaryConstituency (code)', ''),
        ],
        'filename': 'Constituency',
        'make_charts': False,
        },
    ]

essential_columns = [
    ('Phase', '2020-21'), 
    ('Change in spending power with 2015-16', '2020-21'),
    ('Change in spending power with 2015-16 (%)', '2020-21'),
    ]
funding_out = funding.dropna(subset=essential_columns)
agg = {
       ('EstablishmentName', ''): 'count',
       }
for year in ['2015-16', '2020-21']:
    agg[('Pupils', year)] = 'sum'
for year in ['2015-16', '2020-21']:
    agg[('Grant Funding (2022-23 prices)', year)] = 'sum'
agg[('Schools with cut in spending power', '2020-21')] = 'mean'

for group in groups:
    summary = funding_out.groupby(group['groupby']).agg(agg)
    summary.rename(
        columns={'EstablishmentName': 'Schools'},
        inplace=True
        )
    for year in ['2015-16', '2020-21']:
        summary[('Grant Funding Per Pupil (2022-23 prices)', year)] = (
            summary[('Grant Funding (2022-23 prices)', year)] /
            summary[('Pupils', year)]
            )
    summary[('Change in per pupil funding with 2015-16', '2020-21')] = (
        summary[('Grant Funding Per Pupil (2022-23 prices)'), '2020-21'] -
        summary[('Grant Funding Per Pupil (2022-23 prices)'), '2015-16']
        )
    summary[('Change in spending power with 2015-16 (%)', '2020-21')] = (
        summary[('Grant Funding Per Pupil (2022-23 prices)'), '2020-21'] /
        summary[('Grant Funding Per Pupil (2022-23 prices)'), '2015-16'] - 1
        )
    summary.index.names = [ind[0] for ind in summary.index.names]
    writer = ExcelWriter(
        f"{output_dir}/{group['filename']}.xlsx",
        engine='xlsxwriter',
    )
    summary.to_excel(writer, 'Data')
    worksheet = writer.sheets['Data']
    workbook = writer.book
    index_format = workbook.add_format()
    index_format.set_align('top')
    index_format.set_align('left')
    index_format.set_bold()
    index_format.set_border()
    percent= workbook.add_format()
    percent.set_num_format('0%')
    gbp = workbook.add_format()
    gbp.set_num_format('"£"#,##0')
    gbp_m = workbook.add_format()
    gbp_m.set_num_format('"£"0.0,," mn";-"£"0.0,," mn"')
    int_format = workbook.add_format()
    int_format.set_num_format('#,##0')
    col_offset = len(summary.index.names)-1
    worksheet.set_column(0, col_offset, 20, index_format)
    worksheet.set_column(col_offset+1, col_offset+3, 10, int_format)
    worksheet.set_column(col_offset+4, col_offset+5, 10, gbp_m)
    worksheet.set_column(col_offset+6, col_offset+6, 10, percent)
    worksheet.set_column(col_offset+7, col_offset+9, 10, gbp)
    worksheet.set_column(col_offset+10, col_offset+10, 10, percent)
    worksheet.freeze_panes(3, col_offset+1)
    writer.close()

funding_out = funding[
    [
        (                        'EstablishmentName',        ''),
        (                                'LA (name)',        ''),
        (                            'Trusts (name)',        ''),
        (                               'GOR (name)',        ''),
        (            'DistrictAdministrative (name)',        ''),
        (         'ParliamentaryConstituency (name)',        ''),
        (                   'Free School Meals band',        ''),
        (                                    'Phase', '2020-21'),
        (                                   'Pupils', '2015-16'),
        (                                   'Pupils', '2016-17'),
        (                                   'Pupils', '2017-18'),
        (                                   'Pupils', '2018-19'),
        (                                   'Pupils', '2019-20'),
        (                                   'Pupils', '2020-21'),
        (                            'Grant Funding', '2015-16'),
        (                            'Grant Funding', '2016-17'),
        (                            'Grant Funding', '2017-18'),
        (                            'Grant Funding', '2018-19'),
        (                            'Grant Funding', '2019-20'),
        (                            'Grant Funding', '2020-21'),
        (           'Grant Funding (2022-23 prices)', '2015-16'),
        (           'Grant Funding (2022-23 prices)', '2016-17'),
        (           'Grant Funding (2022-23 prices)', '2017-18'),
        (           'Grant Funding (2022-23 prices)', '2018-19'),
        (           'Grant Funding (2022-23 prices)', '2019-20'),
        (           'Grant Funding (2022-23 prices)', '2020-21'),
        ( 'Grant Funding Per Pupil (2022-23 prices)', '2015-16'),
        ( 'Grant Funding Per Pupil (2022-23 prices)', '2016-17'),
        ( 'Grant Funding Per Pupil (2022-23 prices)', '2017-18'),
        ( 'Grant Funding Per Pupil (2022-23 prices)', '2018-19'),
        ( 'Grant Funding Per Pupil (2022-23 prices)', '2019-20'),
        ( 'Grant Funding Per Pupil (2022-23 prices)', '2020-21'),
        (    'Change in spending power with 2015-16', '2016-17'),
        (    'Change in spending power with 2015-16', '2017-18'),
        (    'Change in spending power with 2015-16', '2018-19'),
        (    'Change in spending power with 2015-16', '2019-20'),
        (    'Change in spending power with 2015-16', '2020-21'),
        ('Change in spending power with 2015-16 (%)', '2016-17'),
        ('Change in spending power with 2015-16 (%)', '2017-18'),
        ('Change in spending power with 2015-16 (%)', '2018-19'),
        ('Change in spending power with 2015-16 (%)', '2019-20'),
        ('Change in spending power with 2015-16 (%)', '2020-21'),
        ]
    ].copy()
funding_out.dropna(subset=[('Phase', '2020-21')], inplace=True)
columns_rename = []
for col in funding_out.columns:
    if col[1]=='':
        columns_rename.append(col[0])
    else:
        columns_rename.append(f'{col[0]}\n{col[1]}')
funding_out.columns = columns_rename
columns_rename = {
    'EstablishmentName': 'School',
    'LA (name)': 'Local Authority',
    'Trusts (name)': 'Trust',
    'GOR (name)': 'Region',
    'DistrictAdministrative (name)': 'District',
    'ParliamentaryConstituency (name)': 'Constituency',
    }
funding_out.rename(columns=columns_rename, inplace=True)
writer = ExcelWriter(
    f"{output_dir}/All schools.xlsx",
    engine='xlsxwriter',
    )
funding_out.to_excel(
    writer, 
    sheet_name='Data', 
    startrow=1, 
    header=False, 
    index=False
    )
worksheet = writer.sheets['Data']
workbook = writer.book
index_format = workbook.add_format()
index_format.set_align('center')
index_format.set_align('left')
index_format.set_bold()
index_format.set_border()
index_format.set_text_wrap()
percent= workbook.add_format()
percent.set_num_format('0%')
gbp = workbook.add_format()
gbp.set_num_format('"£"#,##0')
int_format = workbook.add_format()
int_format.set_num_format('#,##0')
worksheet.set_column(0, 0, 50, index_format)
worksheet.set_column(1, 5, 20, int_format)
worksheet.set_column(6, 13, 10, int_format)
worksheet.set_column(14, 36, 15, gbp)
worksheet.set_column(37, 41, 15, percent)
worksheet.freeze_panes(1, 1)
for col, name in enumerate(funding_out.columns):
    worksheet.write(0, col, name, index_format)
writer.close()
