
# from palettable.colorbrewer.sequential import Blues_8
# palette_2021 = Blues_8.hex_colors

import pyvis
import pandas as pd
from pyvis.network import Network

# Color categories: First three weeks, Middle three weeks, Last two weeks
palette_2021 = [['#e3342f', '#e3342f', '#e3342f', '#f7806f', '#f7806f', '#f7806f', '#ffB99f', '#ffB99f'],
             ['#f6993f', '#f6993f', '#f6993f', '#fac97f', '#fac97f', '#fac97f', '#fdec6f', '#fdec6f'],
             ['#ffed4a', '#ffed4a','#ffed4a','#fff88a', '#fff88a','#fff88a','#ffffba', '#ffffba'],
             ['#38c172', '#38c172', '#38c172', '#7dd2b2', '#7dd2b2', '#7dd2b2', '#b3dee2', '#b3dee2'],
             ['#4dc0b5', '#4dc0b5', '#4dc0b5', '#91d0d9', '#91d0d9', '#91d0d9', '#c4dcf4', '#c4dcf4'],
             ['#3490dc', '#3490dc', '#3490dc', '#89a8ec', '#89a8ec', '#89a8ec', '#c8c0f8', '#c8c0f8'],
             ['#6574cd', '#6574cd', '#6574cd', '#95a4f1', '#95a4f1', '#95a4f1', '#b9bcff', '#b9bcff'],
             ['#9561e2', '#9561e2', '#9561e2', '#bd91fa', '#bd91fa', '#bd91fa', '#dbb5ff', '#dbb5ff'],
             ['#f66d9b', '#f66d9b', '#f66d9b', '#fa9dbb', '#fa9dbb', '#fa9dbb', '#fdc1d3', '#fdc1d3']]
# from palettable.colorbrewer.sequential import Blues_9
# palette_2022 = Blues_9.hex_colors
# palette_2022.reverse()
# palette_2022.append('#FAF6F0')

# Color categories: First three weeks, Middle three weeks, Last four weeks
palette_2022 = [['#e3342f', '#e3342f', '#e3342f', '#f7806f', '#f7806f', '#f7806f', '#ffB99f', '#ffB99f', '#ffB99f', '#ffB99f'],
             ['#f6993f', '#f6993f', '#f6993f', '#fac97f', '#fac97f', '#fac97f', '#fdec6f', '#fdec6f', '#fdec6f', '#fdec6f'],
             ['#ffed4a', '#ffed4a','#ffed4a','#fff88a', '#fff88a','#fff88a','#ffffba', '#ffffba', '#ffffba', '#ffffba'],
             ['#38c172', '#38c172', '#38c172', '#7dd2b2', '#7dd2b2', '#7dd2b2', '#b3dee2', '#b3dee2', '#b3dee2', '#b3dee2'],
             ['#4dc0b5', '#4dc0b5', '#4dc0b5', '#91d0d9', '#91d0d9', '#91d0d9', '#c4dcf4', '#c4dcf4', '#c4dcf4', '#c4dcf4'],
             ['#3490dc', '#3490dc', '#3490dc', '#89a8ec', '#89a8ec', '#89a8ec', '#c8c0f8', '#c8c0f8', '#c8c0f8', '#c8c0f8'],
             ['#6574cd', '#6574cd', '#6574cd', '#95a4f1', '#95a4f1', '#95a4f1', '#b9bcff', '#b9bcff', '#b9bcff', '#b9bcff'],
             ['#9561e2', '#9561e2', '#9561e2', '#bd91fa', '#bd91fa', '#bd91fa', '#dbb5ff', '#dbb5ff', '#dbb5ff', '#dbb5ff'],
             ['#f66d9b', '#f66d9b', '#f66d9b', '#fa9dbb', '#fa9dbb', '#fa9dbb', '#fdc1d3', '#fdc1d3', '#fdc1d3', '#fdc1d3']]
# from palettable.colorbrewer.sequential import Blues_5
# palette_2023 = Blues_5.hex_colors

palette_2023 = [['#e3342f', '#e3342f', '#e3342f', '#f7806f', '#f7806f', '#f7806f', '#ffB99f', '#ffB99f', '#ffB99f'],
             ['#f6993f', '#f6993f', '#f6993f', '#fac97f', '#fac97f', '#fac97f', '#fdec6f', '#fdec6f', '#fdec6f'],
             ['#ffed4a', '#ffed4a','#ffed4a','#fff88a', '#fff88a','#fff88a','#ffffba', '#ffffba', '#ffffba'],
             ['#38c172', '#38c172', '#38c172', '#7dd2b2', '#7dd2b2', '#7dd2b2', '#b3dee2', '#b3dee2', '#b3dee2'],
             ['#4dc0b5', '#4dc0b5', '#4dc0b5', '#91d0d9', '#91d0d9', '#91d0d9', '#c4dcf4', '#c4dcf4', '#c4dcf4'],
             ['#3490dc', '#3490dc', '#3490dc', '#89a8ec', '#89a8ec', '#89a8ec', '#c8c0f8', '#c8c0f8', '#c8c0f8'],
             ['#6574cd', '#6574cd', '#6574cd', '#95a4f1', '#95a4f1', '#95a4f1', '#b9bcff', '#b9bcff', '#b9bcff'],
             ['#9561e2', '#9561e2', '#9561e2', '#bd91fa', '#bd91fa', '#bd91fa', '#dbb5ff', '#dbb5ff', '#dbb5ff'],
             ['#f66d9b', '#f66d9b', '#f66d9b', '#fa9dbb', '#fa9dbb', '#fa9dbb', '#fdc1d3', '#fdc1d3', '#fdc1d3']]
keyword_category = pd.read_excel("assets/dictionary 2.0.xlsx", index_col=0).iloc[:, 0:1]

file_names_2021 = ['Y2021_Student01', 'Y2021_Student02', 'Y2021_Student03', 'Y2021_Student04', 'Y2021_Student05',
                   'Y2021_Student06', 'Y2021_Student07']
year2021_df = []
for i in range(len(file_names_2021)):
    temp_df = pd.read_csv("assets/Year2021/" + file_names_2021[i] + ".csv", index_col=0)
    year2021_df.append(temp_df)

file_names_2022 = ['Y2022_Student01', 'Y2022_Student02', 'Y2022_Student03', 'Y2022_Student04', 'Y2022_Student05',
                   'Y2022_Student06', 'Y2022_Student07', 'Y2022_Student08', 'Y2022_Student09', 'Y2022_Student10',
                   'Y2022_Student11', 'Y2022_Student12']
year2022_df = []
for i in range(len(file_names_2022)):
    temp_df = pd.read_csv("assets/Year2022/" + file_names_2022[i] + ".csv", index_col=0)
    year2022_df.append(temp_df)

file_names_2023 = ['Y2023_Student01', 'Y2023_Student02', 'Y2023_Student03', 'Y2023_Student04', 'Y2023_Student05',
                   'Y2023_Student06', 'Y2023_Student07', 'Y2023_Student08', 'Y2023_Student09', 'Y2023_Student10',
                   'Y2023_Student11', 'Y2023_Student12']
year2023_df = []
for i in range(len(file_names_2023)):
    temp_df = pd.read_csv("assets/Year2023/" + file_names_2023[i] + ".csv", index_col=0)
    year2023_df.append(temp_df)

keywords = list(year2021_df[0].head())

# the number shows which category the keyword belongs to
keywords_group = keyword_category.iloc[:, 0].to_numpy()


def aggregate_individual_knowledge_map(student_df, color_plate):
    nets = []
    for i in range(student_df.shape[0]):
        net = Network(notebook=True)#, heading="Individual Knowledge Map Aggregate Week " + str(i+1))
        occurence = student_df.iloc[:(i + 1)].sum()
        for n in range(i + 1):
            for j, value in enumerate(student_df.iloc[n]):
                if value == 1:
                    category_number = keywords_group[j] - 1
                    net.add_node(j, label=keywords[j], title='Week' + str(n + 1), size=(int(occurence[j]) + 1) * 3,
                                 color=color_plate[category_number][n])
        net_id = [dic['id'] for dic in net.nodes]
        for i in net_id:
            for j in net_id:
                if i != j and keywords_group[i] == keywords_group[j]:
                    net.add_edge(i, j, hidden=True)
        net.repulsion(central_gravity=1, spring_length=50)
        nets.append(net)

    return nets


indi_aggregate_s1_2021 = aggregate_individual_knowledge_map(year2021_df[0], palette_2021)
indi_aggregate_s2_2021 = aggregate_individual_knowledge_map(year2021_df[1], palette_2021)
indi_aggregate_s3_2021 = aggregate_individual_knowledge_map(year2021_df[2], palette_2021)
indi_aggregate_s4_2021 = aggregate_individual_knowledge_map(year2021_df[3], palette_2021)
indi_aggregate_s5_2021 = aggregate_individual_knowledge_map(year2021_df[4], palette_2021)
indi_aggregate_s6_2021 = aggregate_individual_knowledge_map(year2021_df[5], palette_2021)
indi_aggregate_s7_2021 = aggregate_individual_knowledge_map(year2021_df[6], palette_2021)

indi_aggregate_s1_2022 = aggregate_individual_knowledge_map(year2022_df[0], palette_2022)
indi_aggregate_s2_2022 = aggregate_individual_knowledge_map(year2022_df[1], palette_2022)
indi_aggregate_s3_2022 = aggregate_individual_knowledge_map(year2022_df[2], palette_2022)
indi_aggregate_s4_2022 = aggregate_individual_knowledge_map(year2022_df[3], palette_2022)
indi_aggregate_s5_2022 = aggregate_individual_knowledge_map(year2022_df[4], palette_2022)
indi_aggregate_s6_2022 = aggregate_individual_knowledge_map(year2022_df[5], palette_2022)
indi_aggregate_s7_2022 = aggregate_individual_knowledge_map(year2022_df[6], palette_2022)
indi_aggregate_s8_2022 = aggregate_individual_knowledge_map(year2022_df[7], palette_2022)
indi_aggregate_s9_2022 = aggregate_individual_knowledge_map(year2022_df[8], palette_2022)
indi_aggregate_s10_2022 = aggregate_individual_knowledge_map(year2022_df[9], palette_2022)
indi_aggregate_s11_2022 = aggregate_individual_knowledge_map(year2022_df[10], palette_2022)
indi_aggregate_s12_2022 = aggregate_individual_knowledge_map(year2022_df[11], palette_2022)

indi_aggregate_s1_2023 = aggregate_individual_knowledge_map(year2023_df[0], palette_2023)
indi_aggregate_s2_2023 = aggregate_individual_knowledge_map(year2023_df[1], palette_2023)
indi_aggregate_s3_2023 = aggregate_individual_knowledge_map(year2023_df[2], palette_2023)
indi_aggregate_s4_2023 = aggregate_individual_knowledge_map(year2023_df[3], palette_2023)
indi_aggregate_s5_2023 = aggregate_individual_knowledge_map(year2023_df[4], palette_2023)
indi_aggregate_s6_2023 = aggregate_individual_knowledge_map(year2023_df[5], palette_2023)
indi_aggregate_s7_2023 = aggregate_individual_knowledge_map(year2023_df[6], palette_2023)
indi_aggregate_s8_2023 = aggregate_individual_knowledge_map(year2023_df[7], palette_2023)
indi_aggregate_s9_2023 = aggregate_individual_knowledge_map(year2023_df[8], palette_2023)
indi_aggregate_s10_2023 = aggregate_individual_knowledge_map(year2023_df[9], palette_2023)
indi_aggregate_s11_2023 = aggregate_individual_knowledge_map(year2023_df[10], palette_2023)
indi_aggregate_s12_2023 = aggregate_individual_knowledge_map(year2023_df[11], palette_2023)



for s in range(1, 13):
    for i, indi_aggregate in enumerate(globals()[f"indi_aggregate_s{s}_2023"]):
        indi_aggregate.show(f"assets/2023_s{s}_aggregate_{i+1}.html")
for s in range(1, 13):
    for i, indi_aggregate in enumerate(globals()[f"indi_aggregate_s{s}_2022"]):
        indi_aggregate.show(f"assets/2022_s{s}_aggregate_{i+1}.html")
for s in range(1, 8):
    for i, indi_aggregate in enumerate(globals()[f"indi_aggregate_s{s}_2021"]):
        indi_aggregate.show(f"assets/2021_s{s}_aggregate_{i+1}.html")