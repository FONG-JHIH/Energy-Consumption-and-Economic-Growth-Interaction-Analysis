import pandas as pd

# 文件路径列表（请确认路径是否正确）
file_paths = [
    r"行業別用電_2019.csv",
    r"行業別用電_2020.csv",
    r"行業別用電_2021.csv",
    r"行業別用電_2022.csv",
    r"行業別用電_2023.csv"
]

# 定义一个空列表来存储数据
dataframes = []

# 读取并清理每个文件
for file in file_paths:
    try:
        # 读取CSV文件
        df = pd.read_csv(file, encoding='utf-8')
        
        # 去除多余的空白字符
        df.columns = df.columns.str.strip()
        
        # 假设CSV中有'行業別中類', '行業別小類', '用電量'等列
        # 使用行業別中類填补行業別小類的缺失值
        df['行業別小類'].fillna(df['行業別中類'], inplace=True)
        
        # 添加年份信息
        year = file.split('_')[-1].split('.')[0]  # 从文件名中提取年份
        df['年份'] = int(year)
        
        # 将清理后的DataFrame添加到列表中
        dataframes.append(df)
    except FileNotFoundError:
        print(f"文件 {file} 未找到，请检查路径是否正确。")
    except Exception as e:
        print(f"读取文件 {file} 时发生错误: {e}")

# 合并所有年份的数据
if dataframes:
    merged_data = pd.concat(dataframes, ignore_index=True)

    # 导出清理后的数据到新的CSV文件
    cleaned_file_path = "Industry_electricity.csv"
    merged_data.to_csv(cleaned_file_path, index=False)
    print(f"清理後的數據已保存到 {cleaned_file_path}")
else:
    print("未读取到任何数据，请检查文件路径。")
    
#%%
import pandas as pd

# 讀取CSV檔案
file_path = "國內生產毛額(名目金額)-按行業分Report.csv"
df = pd.read_csv(file_path)


# 清理數據
# 刪除第一行單位說明，並使用第二行作為標題
df.columns = df.iloc[1]
df = df[2:]

# 將「年」欄位重命名為「Year」並轉換為西元年
df = df.rename(columns={"年": "Year"})
df["Year"] = df["Year"].str.replace("年", "").astype(int) + 1911

# 清理欄位名稱，移除多餘空白和換行符號
df.columns = df.columns.str.replace("\n", "").str.replace(" ", "")

# 去除數字中的空格並轉換為浮點數格式
for col in df.columns[1:]:
    df[col] = df[col].str.replace(",", "").str.replace(" ", "").astype(float)

# 檢查並處理缺失值（可根據需要選擇填補或刪除缺失值，此處選擇填充為0）
df = df.fillna(0)

# 將清理後的數據保存到新的CSV文件
output_path = "GDP by industry Report.csv"
df.to_csv(output_path, index=False)

print(f"數據清理完成，結果已保存到 {output_path}")


#%%
# 匯入所需的資料庫
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

# 中文的基本設定（影響全局字體顯示）
plt.rcParams['font.family'] = 'Microsoft YaHei'  # 設定字體為 'Microsoft YaHei'
plt.rcParams['font.size'] = 12  # 設定字體大小為 12

# 指定特定字體的設定（適用於指定元素）
font_path = 'C:\\Windows\\Fonts\\msjhl.ttc'  # 指定標楷體字體文件的路徑
font_prop = fm.FontProperties(fname=font_path)
font_prop.set_style('normal')  # 設定字體樣式為正常
font_prop.set_size(12)  # 設定字體大小

# 定義 CSV 文件的路徑
gdp_file = 'GDP by industry Report.csv'
electricity_file = 'Industry_electricity.csv'

# 使用 pandas 讀取 'GDP by industry Report.csv' 的數據
gdp_data_df = pd.read_csv(gdp_file, encoding='utf-8')

# 使用 pandas 讀取 'Industry_electricity.csv' 的數據
electricity_usage_df = pd.read_csv(electricity_file, encoding='utf-8')

# 顯示前幾行數據以確認加載成功
print("GDP by Industry Data Preview:")
print(gdp_data_df.head())

print("\nIndustry Electricity Usage Data Preview:")
print(electricity_usage_df.head())

#%%

# 過濾出 2019 到 2023 年之間的數據
filtered_gdp_data_df = gdp_data_df[gdp_data_df['Year'].between(2019, 2023)]

# 移除 "總GDP" 列，因為我們只關心各個行業的 GDP 數據
sector_gdp_data = filtered_gdp_data_df.drop(columns=['總GDP'])

# 創建一個新 DataFrame 來存儲每年 GDP 排名前五位的行業
top_5_gdp_sectors_per_year = pd.DataFrame()

# 找出每一年 GDP 排名前五位的行業並將結果合併到一個 DataFrame 中
for year in range(2019, 2024):
    # 設定年份為索引並轉置數據，以便挑選前五大行業
    top_5_sectors = sector_gdp_data[sector_gdp_data['Year'] == year].set_index('Year').T.nlargest(5, year)
    # 合併到主 DataFrame 中
    top_5_gdp_sectors_per_year = pd.concat([top_5_gdp_sectors_per_year, top_5_sectors], axis=1)

# 準備面積圖的數據
top_5_gdp_sectors_per_year = top_5_gdp_sectors_per_year.T  # 轉置數據以便繪製
years = top_5_gdp_sectors_per_year.index  # 提取年份作為 X 軸數據

# 繪製面積圖
plt.figure(figsize=(12, 8))
plt.stackplot(years, top_5_gdp_sectors_per_year.values.T, labels=top_5_gdp_sectors_per_year.columns, alpha=0.8)
plt.title("2019-2023年GDP前五大行業面積圖", fontsize=16)
plt.xlabel("年份", fontsize=12)
plt.ylabel("GDP (百萬元)", fontsize=12)
plt.legend(title="行業別", loc='upper left')
plt.tight_layout()

# 顯示圖表
plt.show()

#%%
# 過濾 2019 年到 2023 年之間的數據，並只選擇製造業（C.製造業）的用電數據
filtered_electricity_usage_df = electricity_usage_df[
    (electricity_usage_df['行業別大類'] == 'C.製造業') &  # 條件：行業大類為 "C.製造業"
    (electricity_usage_df['年份'] >= 2019) &  # 條件：年份大於或等於 2019
    (electricity_usage_df['年份'] <= 2023)  # 條件：年份小於或等於 2023
]

# 過濾 GDP 數據集中 2019 到 2023 年的數據
filtered_gdp_data_df = gdp_data_df[gdp_data_df['Year'].between(2019, 2023)]  # 選擇 2019-2023 年

# 將過濾後的用電數據按年份分組，並計算每年的製造業總用電量
annual_electricity_usage = filtered_electricity_usage_df.groupby('年份')['用電量'].sum()

# 從過濾後的 GDP 數據中提取製造業 GDP 的數值，並將年份設為索引
annual_gdp = filtered_gdp_data_df.set_index('Year')['製造業GDP']

# 確保兩個數據序列擁有相同的年份，以便進行比較和可視化
years = np.intersect1d(annual_electricity_usage.index, annual_gdp.index)

# 將數據轉換為 NumPy 陣列，以便進行相關性分析和繪圖
electricity_usage_values = annual_electricity_usage[years].values  # 提取用電量數據
gdp_values = annual_gdp[years].values  # 提取 GDP 數據

# 計算製造業的用電量和 GDP 之間的相關性係數
correlation = np.corrcoef(electricity_usage_values, gdp_values)[0, 1]

# 開始繪圖
plt.figure(figsize=(10, 6))  # 設定圖表大小

# 繪製用電量數據，使用藍色線條和圓形標記
plt.plot(years, electricity_usage_values, label="用電量(MWh)", marker='o', color='blue')

# 繪製 GDP 數據，使用綠色線條和圓形標記
plt.plot(years, gdp_values, label="製造業 GDP (NT$)", marker='o', color='green')

# 添加標題和標籤，顯示兩者的相關性
plt.title(f"製造業 (C) 用電量與 GDP（2019-2023）\n相關性係數Correlation: {correlation:.2f}")
plt.xlabel("年份",fontproperties=font_prop)  # X 軸標籤為年份
plt.ylabel("數值",fontproperties=font_prop, rotation=0, ha='right')  # Y 軸標籤為數值

# 添加圖例
plt.legend()

# 顯示網格線
plt.grid(True)

# 顯示圖表
plt.show()

#%%
# 定義一致的顏色映射，為每個行業分配固定顏色
industry_categories = sorted(electricity_usage_df['行業別中類'].unique())
colors = plt.get_cmap('tab20').colors  # 使用 'tab20' 調色盤
colors_map = {category: colors[i % len(colors)] for i, category in enumerate(industry_categories)}

# 過濾出 2019 到 2023 年之間的數據，並且只選擇 "C.製造業"
filtered_electricity_data = electricity_usage_df[
    (electricity_usage_df['行業別大類'] == 'C.製造業') &
    (electricity_usage_df['年份'].between(2019, 2023))
]

# 計算每個年份內各行業中類的用電量總和
industry_usage_by_year = filtered_electricity_data.groupby(['年份', '行業別中類'])['用電量'].sum().unstack().fillna(0)

# 準備面積圖的數據
years = industry_usage_by_year.index  # 提取年份作為 X 軸數據

# 繪製面積圖，使用統一的顏色映射
plt.figure(figsize=(14, 8))
plt.stackplot(
    years,
    [industry_usage_by_year[industry] for industry in industry_usage_by_year.columns],
    labels=industry_usage_by_year.columns,
    colors=[colors_map[industry] for industry in industry_usage_by_year.columns],  # 使用固定的顏色
    alpha=0.8
)

# 添加標題、軸標籤和圖例
plt.title("2019-2023年製造業各行業用電量變化趨勢", fontsize=16)
plt.xlabel("年份", fontsize=12)
plt.ylabel("用電量 (MWh)", fontsize=12)
plt.legend(title="製造業各行業種類", loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

# 計算每一年中各行業用電量的百分比
industry_usage_percentage = industry_usage_by_year.div(industry_usage_by_year.sum(axis=1), axis=0)
cumulative_percentage = industry_usage_percentage.cumsum(axis=1)

# 創建橫向的Marimekko圖表
plt.figure(figsize=(20, 12))
for industry in industry_usage_percentage.columns:
    heights = industry_usage_percentage[industry]
    left = cumulative_percentage[industry] - heights
    plt.barh(
        industry_usage_percentage.index,
        heights,
        left=left,
        label=industry,
        color=colors_map[industry]  # 使用固定的顏色
    )

# 在前3大百分比的位置顯示百分比數值
for year in industry_usage_percentage.index:
    top_3 = industry_usage_percentage.loc[year].nlargest(3)
    for industry in top_3.index:
        value = top_3[industry] * 100
        left_position = cumulative_percentage.loc[year, industry] - industry_usage_percentage.loc[year, industry] / 2
        plt.text(
            left_position,
            year,
            f"{value:.1f}%",
            ha='center', va='center', fontsize=9, color='black'
        )

# 添加標題、軸標籤和圖例
plt.title("2019-2023年製造業各行業用電量百分比堆積圖", fontsize=16)
plt.ylabel("年份", fontsize=12)
plt.xlabel("用電量占比 (%)", fontsize=12)
plt.legend(title="製造業各行業種類", loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=5)
plt.tight_layout(rect=[0, 0.2, 1, 1])
plt.show()

#%%
import pandas as pd

# 读取CSV文件
file_path = "Industry_electricity.csv"  # 替换为你的文件路径
electricity_data = pd.read_csv(file_path)

# 筛选数据：年份为2019至2023，行业小类为261、262、263、264、269
filtered_data = electricity_data[
    (electricity_data["年份"].between(2019, 2023)) &
    (electricity_data["行業別小類"].str.contains("261|262|263|264|269"))
]

# 按照年份、月份和行业小类汇总用电量
monthly_usage = filtered_data.groupby(["年份", "月份", "行業別小類"])["用電量"].sum().reset_index()

# 透视表：行是（年份，月份），列是行业小类，值是用电量
pivot_data = monthly_usage.pivot_table(
    index=["年份", "月份"],
    columns="行業別小類",
    values="用電量",
    fill_value=0
)

# 保存结果为CSV文件
output_file_path = "Electricity_Usage_2019_2023.csv"
pivot_data.to_csv(output_file_path)

print(f"数据已保存至：{output_file_path}")
# 引入必要的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 定義 CSV 文件的路徑
electricity_file = 'Electricity_Usage_2019_2023.csv'

# 使用 pandas 讀取數據
electricity_usage_df = pd.read_csv(electricity_file, encoding='utf8')

# 創建樞紐表來匯總各行業每年的用電量
electricity_pivot = electricity_usage_df.groupby(['年份']).sum()

# 行業別列表，用於排序和顯示
industries = [
    "261 半導體製造業", 
    "262 被動電子元件製造業", 
    "263 印刷電路板製造業", 
    "264 光電材料及元件製造業", 
    "269 其他電子零組件製造業"
]

# 過濾數據，只保留相關行業
electricity_pivot = electricity_pivot[industries]

# 自定義暖色系調色板
custom_colors = ['#FFB74D', '#FF8A65', '#F06292', '#BA68C8', '#64B5F6']

# 畫堆疊長條圖，使用自定義的顏色
plt.figure(figsize=(10, 6))
electricity_pivot.plot(
    kind='bar',
    stacked=True,
    color=custom_colors,  # 使用自定義顏色列表
    width=0.7,
    edgecolor='black'
)
plt.title('2019-2023 年各電子零組件製造業用電量對比', fontsize=14)
plt.xlabel('年份', fontsize=12)
plt.ylabel('用電量 (千瓦時)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='行業別小類', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

