import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('.\data\Cleaned_Road_Accident_Data.csv')

fig, axes = plt.subplots(
    2,
    3,
    figsize=(20,12)
)

fig.suptitle(
    "Road Accident Analysis Dashboard",
    fontsize=20,
    fontweight='bold'
)

# 1 Severity
sns.countplot(
    y='Accident_Severity',
    data=df,
    ax=axes[0,0]
)

axes[0,0].set_title("Accident Severity")

# 2 Day of Week

order = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

sns.countplot(
    x='Day_of_Week',
    data=df,
    order=order,
    ax=axes[0,1]
)

axes[0,1].tick_params(
    axis='x',
    rotation=45
)

axes[0,1].set_title("Accidents by Day")

# 3 Hour Distribution

sns.histplot(
    df['Hour'],
    bins=24,
    ax=axes[0,2]
)

axes[0,2].set_title("Accidents by Hour")

# 4 Weather

top_weather = df['Weather_Conditions'] \
                .value_counts() \
                .head(5)

sns.barplot(
    x=top_weather.values,
    y=top_weather.index,
    ax=axes[1,0]
)

axes[1,0].set_title("Top Weather Conditions")

# 5 Urban Rural

sns.countplot(
    x='Urban_or_Rural_Area',
    data=df,
    ax=axes[1,1]
)

axes[1,1].set_title("Urban vs Rural")

# 6 Vehicle Type

top_vehicle = df['Vehicle_Type'] \
                .value_counts() \
                .head(10)

sns.barplot(
    x=top_vehicle.values,
    y=top_vehicle.index,
    ax=axes[1,2]
)

axes[1,2].set_title("Top Vehicle Types")

plt.tight_layout()

plt.savefig(
    "Road_Accident_Dashboard.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()