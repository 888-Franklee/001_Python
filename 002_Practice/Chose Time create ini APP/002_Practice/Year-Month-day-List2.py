from calendar import isleap

years = range(2024, 2029)  # 示例年份范围
months = range(1, 13)  # 月份范围
days = range(1, 32)  # 日期范围

date_list = []

for year in years:
    for month in months:
        for day in days:
            # 判断无效日期
            if (month == 2 and day > 29) or \
               (month == 2 and day == 29 and not isleap(year)) or \
               (month in [4, 6, 9, 11] and day > 30):
                continue  # 跳过无效日期
            date_list.append(f"{year}-{month:02d}-{day:02d}")

# 打印部分结果示例
for date in date_list[:365]:
    print(date)
