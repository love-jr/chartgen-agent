chart_types = [
    'Single broken line',  
    'multiple broken lines (3 to 5 lines)',  
    'single broken line represented by a dotted line',  
    'multiple broken lines represented by dotted lines',  
    'Single Pie Chart',  
    'simple bar chart (horizontal)',  
    'paired bar chart (horizontal)',  
    'simple column chart (vertical)',  
    'paired column chart (vertical)'  
]


"""

chart_types = ['Single broken line', 'multiple broken lines (3 to 5 lines)','single broken line represented by a dotted line',
               'multiple broken lines represented by dotted lines','Single Pie Chart','General bar chart (horizontal)',
               'paired bar chart (horizontal)','General column chart (vertical)','paired column chart (vertical)']

def select_chart_list(chart_topic):
    if chart_topic == "Single broken line":
        return Single_broken_line
    elif chart_topic == "multiple broken lines (3 to 5 lines)":
        return multiple_broken_lines
    elif chart_topic == "single broken line represented by a dotted line":
        return Single_broken_line_dotted
    elif chart_topic == "multiple broken lines represented by dotted lines":
        return multiple_broken_lines_dotted
    elif chart_topic == "Single Pie Chart":
        return Single_Pie_Chart
    elif chart_topic == "simple bar chart (horizontal)":
        return simple_bar_chart
    elif chart_topic == "paired bar chart (horizontal)":
        return paired_bar_chart
    elif chart_topic == "simple column chart (vertical)":
        return simple_column_chart
    elif chart_topic == "paired column chart (vertical)":
        return paired_column_chart
    else:
        return None
               

"""


Single_broken_line = [
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2017, 2018, 2019, 2020, 2021, 2022),
  Interference_Cases = c(5, 8, 10, 15, 18, 22)
)

# Create a more visually appealing plot
grouped_bars_20250306165454 <- ggplot(data, aes(x = Year, y = Interference_Cases)) +
  # Add gradient area under line
  geom_area(alpha = 0.2, fill = "steelblue") +
  # Main line with better styling
  geom_line(color = "#2b8cbe", size = 1.5) +
  # Larger points with custom styling
  geom_point(color = "#084081", size = 5, shape = 21, fill = "white", stroke = 2) +
  # Better positioned labels
  geom_text_repel(
    aes(label = Interference_Cases),
    size = 7,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 10,
    nudge_y = 1.5,
    segment.color = "gray50",
    segment.size = 0.7,
    min.segment.length = 0,
    max.overlaps = Inf,
    direction = "y"
  ) +
  # Improved axis and title formatting
  scale_x_continuous(breaks = data$Year) +
  scale_y_continuous(limits = c(0, 26), breaks = seq(0, 25, 5)) +
  labs(
    x = "Year",
    y = "Number of Cases",
    title = "Trend in Foreign Election Interference Cases",
    subtitle = "Significant increase observed from 2017 to 2022"
  ) + 
  # Enhanced theme with better spacing and formatting
  theme_wsj() + 
  theme(
    text = element_text(size = 20, color = "black"),
    plot.title = element_text(size = 24, face = "bold", hjust = 0.5),
    plot.subtitle = element_text(size = 20, hjust = 0.5, margin = margin(b = 20)),
    axis.title.x = element_text(size = 20, margin = margin(t = 15)),
    axis.title.y = element_text(size = 20, margin = margin(r = 15)),
    axis.text = element_text(size = 20, color = "black"),
    panel.grid.major.y = element_line(color = "gray90", size = 0.5),
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data is sourced from reports by international security agencies and cybersecurity academic research studies.", save_filepath = '/path/to/output/chart/chart_0005/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023),
  Support_Percentage = c(55, 58, 60, 63, 65, 68, 70, 72, 75)
)

grouped_bars_20250306165454 <- ggplot(data, aes(x = Year, y = Support_Percentage)) +
  geom_line(color = "#1E90FF", size = 1.5, alpha = 0.7) +
  geom_point(size = 4, color = "#8B0000", fill = "#8B0000", shape = 21, stroke = 1.2) +
  geom_text_repel(
    aes(label = paste0(Support_Percentage, "%")),
    size = 6,
    fontface = "bold",
    box.padding = 0.5,
    point.padding = 0.7,
    force = 50,
    force_pull = 0.7,
    segment.size = 0.4,
    segment.color = "gray50",
    min.segment.length = 0.5,
    direction = "both",
    nudge_x = 0.3,
    nudge_y = 0.3
  ) +
  scale_x_continuous(
    breaks = data$Year, 
    expand = expansion(mult = c(0.05, 0.05))
  ) +
  scale_y_continuous(
    breaks = seq(50, 80, 5),
    limits = c(50, 80),
    expand = expansion(mult = c(0.05, 0.05))
  ) +
  labs(
    title = "Public Support for Climate Change Policies",
    subtitle = "Steady Increase in Support from 2015 to 2023",
    x = "Year",
    y = "Support Percentage (%)"
  ) +
  theme_few() +
  theme(
    text = element_text(size = 20, family = "sans"),
    plot.title = element_text(size = 22, face = "bold", hjust = 0.5),
    plot.subtitle = element_text(size = 16, hjust = 0.5),
    axis.title = element_text(size = 20),
    axis.text = element_text(size = 18),
    legend.position = "none",
    plot.margin = margin(1, 1, 1, 1, "cm")
  ) +
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Source: Data sourced from Pew Research Center and Gallup Polls", save_filepath = '/path/to/output/chart/chart_0006/chart.png', width_pixels = 896, height_pixels = 630)

""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022),
  Employment_Growth_Percent = c(2.5, 3.1, 3.7, 4.2, 4.8, 5.3, 5.9, 6.5, 7.1, 7.7)
)

employment_trends_20250306165454 <- ggplot(data, aes(x=Year, y=Employment_Growth_Percent)) +
  geom_line(color="#0072B2", size=1.5) +
  geom_point(color="#0072B2", size=4, shape=21, fill="white", stroke=1.5) +
  geom_text_repel(
    aes(label = paste0(Employment_Growth_Percent, "%")),
    size = 7,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 15,
    nudge_y = 0.4,
    segment.size = 0.7,
    segment.color = "gray50",
    min.segment.length = 0.2,
    direction = "y",
    show.legend = FALSE
  ) +
  scale_x_continuous(breaks = seq(2013, 2022, 1), expand = c(0.05, 0.05)) +
  scale_y_continuous(breaks = seq(0, 8, 1), limits = c(0, 9.0), expand = c(0, 0)) +
  labs(
    title = "Digital Transformation Impact on Employment Trends", 
    subtitle = "Emerging tech sectors show job growth over the past decade.",
    x = "Year",
    y = "Employment Growth (%)"
  ) +
  theme_economist() +
  theme(
    plot.title = element_text(size = 24, face = "bold", hjust = 0),
    plot.subtitle = element_text(size = 20, hjust = 0, margin = margin(b = 20)),
    axis.title.x = element_text(size = 20, face = "bold", margin = margin(t = 15)),
    axis.title.y = element_text(size = 20, face = "bold", margin = margin(r = 15)),
    axis.text.x = element_text(size = 20, angle = 0, hjust = 0.5),
    axis.text.y = element_text(size = 20),
    legend.position = "bottom",
    legend.title = element_text(size = 20),
    legend.text = element_text(size = 20),
    panel.grid.major.y = element_line(color = "gray90", size = 0.5),
    panel.grid.minor = element_blank(),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  bbc_style()

finalise_plot(plot_name = employment_trends_20250306165454, source = "Sourse: Data is sourced from ILO and WEF reports on emerging technology employment trends.", save_filepath = '/path/to/output/chart/chart_0019/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Generation = c("Baby Boomers", "Generation X", "Millennials", "Generation Z"),
  Ideal_Family_Size = c(3.6, 3.2, 2.7, 2.5)
)

# Convert Generation to factor with specified levels to maintain order
data$Generation <- factor(data$Generation, 
                          levels = c("Baby Boomers", "Generation X", "Millennials", "Generation Z"))

broken_line_chart <- ggplot(data, aes(x = Generation, y = Ideal_Family_Size, group = 1)) +
  # Add gradient shading under the line
  geom_area(alpha = 0.2, fill = "steelblue") +
  # Improved line with better color
  geom_line(color = "#1F77B4", size = 2) +
  # Larger points with border
  geom_point(size = 5, color = "#1F77B4", fill = "white", shape = 21, stroke = 2) +
  # Better positioned and formatted labels
  geom_text_repel(
    aes(label = sprintf("%.1f", Ideal_Family_Size)),
    size = 8,
    fontface = "bold",
    box.padding = 1,
    point.padding = 0.7,
    force = 10,
    nudge_y = 0.15,
    direction = "y",
    segment.color = "gray50",
    segment.size = 0.7,
    min.segment.length = 0,
    max.overlaps = Inf,
    show.legend = FALSE
  ) +
  # Better axis scaling and breaks
  scale_y_continuous(
    breaks = seq(0, 4, 0.5),
    limits = c(0, 4.2),
    expand = c(0, 0)
  ) +
  # Improved title and labels
  labs(
    title = "Generational Shifts in Ideal Family Size",
    subtitle = "Declining trend from Baby Boomers to Generation Z",
    y = "Average Ideal Family Size",
    caption = "Data shows a consistent decrease in family size preferences across generations"
  ) +
  # Apply theme with improved aesthetics
  theme_ipsum_ps(base_size = 20, base_family = "Arial") +
  theme(
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title.x = element_blank(),
    axis.title.y = element_text(size = 20, margin = margin(r = 15)),
    axis.text.x = element_text(size = 20, angle = 30, hjust = 1),
    axis.text.y = element_text(size = 20),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank(),
    legend.position = "none",
    plot.margin = margin(30, 30, 30, 30)
  ) + 
  theme_par() +
  bbc_style()

finalise_plot(plot_name = broken_line_chart, 
              source = "Source: Based on surveys from sociological research institutions.", 
              save_filepath = '/path/to/output/chart/chart_0021/chart.png', 
              width_pixels = 896, 
              height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
    Year = c(2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023),
    Growth_Rate = c(3.5, 3.7, 3.2, 2.9, 3.8, 4.1, 3.9, 2.3, 5.0, 4.8, 3.6)
)

broken_line_chart <- ggplot(data, aes(x = Year, y = Growth_Rate)) +
    geom_line(size = 2, color = "#3366CC") +
    geom_point(size = 5, color = "#E63946", alpha = 0.8) +
    geom_text_repel(
        aes(label = sprintf("%.1f%%", Growth_Rate)),
        size = 6,
        fontface = "bold",
        box.padding = 0.8,
        point.padding = 0.8,
        force = 15,
        force_pull = 0.2,
        segment.size = 0.7,
        segment.color = "#888888",
        min.segment.length = 0.2,
        max.overlaps = 15,
        direction = "y",
        nudge_x = 0.2,
        show.legend = FALSE
    ) +
    scale_x_continuous(breaks = seq(2013, 2023, 1)) +
    scale_y_continuous(limits = c(1.5, 5.5), breaks = seq(1.5, 5.5, 0.5)) +
    labs(title = "Effect of Fiscal Policies on Economic Growth",
         subtitle = "Economic growth rates fluctuate with changes in fiscal policies",
         x = "Year", 
         y = "Growth Rate (%)") +
    theme_minimal() +
    theme(
        plot.title = element_text(face = "bold", size = 24, margin = margin(b = 15)),
        plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
        axis.title.x = element_text(face = "bold", size = 22, margin = margin(t = 15)),
        axis.title.y = element_text(face = "bold", size = 22, margin = margin(r = 15)),
        axis.text.x = element_text(size = 20, angle = 0, hjust = 0.5),
        axis.text.y = element_text(size = 20),
        panel.grid.minor = element_blank(),
        panel.grid.major = element_line(color = "#EEEEEE"),
        legend.position = "top",
        legend.text = element_text(size = 20),
        legend.title = element_text(size = 22, face = "bold"),
        plot.margin = margin(20, 20, 20, 20)
    ) +
    theme_tufte() +
    bbc_style()

finalise_plot(plot_name = broken_line_chart, source = "Source: Data sourced from World Bank and IMF economic reports, and government fiscal policy papers.", save_filepath = '/path/to/output/chart/chart_0030/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  FamilyStructure = c("Single", "Married", "Widowed"),
  LifeExpectancy = c(75, 80, 77)
)

line_chart_20250306165454 <- ggplot(data, aes(x = FamilyStructure, y = LifeExpectancy, group = 1)) +
  geom_line(color = "#0072B2", size = 2, linetype = "solid") +
  geom_point(size = 5, color = "#0072B2", fill = "white", shape = 21, stroke = 2) +
  geom_text_repel(
    aes(label = paste0(LifeExpectancy, " years")),
    size = 7,
    fontface = "bold",
    box.padding = 1.5,
    point.padding = 1.5,
    force = 40,
    force_pull = 0.3,
    segment.size = 0.7,
    segment.color = "gray50",
    min.segment.length = 0.2,
    direction = "y",
    nudge_y = 1.5,
    show.legend = FALSE
  ) +
  scale_y_continuous(limits = c(70, 85), breaks = seq(70, 85, 5)) +
  labs(
    title = "Impact of Family Structure on Life Expectancy",
    subtitle = "Married individuals show highest life expectancy",
    x = "Family Structure",
    y = "Life Expectancy (Years)"
  ) +
  theme_minimal(base_size = 20) +
  theme(
    plot.title = element_text(hjust = 0.5, size = 24, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(hjust = 0.5, size = 20, margin = margin(b = 20)),
    axis.title.x = element_text(size = 22, margin = margin(t = 15)),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.text = element_text(size = 20, face = "bold"),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_line(color = "gray90", linetype = "dashed"),
    plot.margin = margin(t = 20, r = 30, b = 20, l = 30)
  ) +
  theme_excel() +
  bbc_style()

finalise_plot(plot_name = line_chart_20250306165454, source = "Sourse: Estimated data based on studies from Population Reference Bureau and health surveys.", save_filepath = '/path/to/output/chart/chart_0036/chart.png', width_pixels = 896, height_pixels = 630)
"""
]

multiple_broken_lines =[
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2020, 2021, 2022, 2023),
  TikTok = c(5.0, 6.7, 7.3, 8.0),
  Instagram_Reels = c(3.4, 4.5, 5.1, 6.0),
  SnapChat = c(2.8, 3.2, 3.7, 4.0)
)

data_long <- reshape2::melt(data, id.vars = "Year", variable.name = "Platform", value.name = "Engagement")

# Improve platform names display
data_long$Platform <- gsub("_", " ", data_long$Platform)

engagement_trends <- ggplot(data_long, aes(x = Year, y = Engagement, color = Platform, group = Platform)) +
  geom_line(size = 1.5) +
  geom_point(size = 4, aes(shape = Platform)) +
  geom_text_repel(
    aes(label = Engagement),
    size = 8,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 15,
    force_pull = 0.2,
    segment.size = 0.7,
    segment.color = "gray50",
    min.segment.length = 0.3,
    direction = "both",
   
    show.legend = FALSE
  ) +
  scale_color_npg(name = "Platform") +
  scale_shape_manual(values = c(16, 17, 18)) +
  scale_y_continuous(limits = c(2, 9), breaks = seq(2, 9, 1)) +
  scale_x_continuous(breaks = c(2020, 2021, 2022, 2023)) +
  labs(
    title = "User Engagement Trends on Video Platforms",
    subtitle = "TikTok leads growth while Instagram Reels and SnapChat steadily increase",
    y = "Engagement (hours/week)",
    x = "Year"
  ) +
  theme_few() +
  theme(
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 10)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title = element_text(size = 20, face = "bold"),
    axis.text = element_text(size = 20),
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box.spacing = unit(1, "cm"),
    legend.text = element_text(size = 20),
    legend.key.size = unit(1.5, "cm"),
    legend.spacing.x = unit(0.5, "cm"),
    panel.grid.major = element_line(color = "gray90"),
    panel.grid.minor = element_blank()
  ) +
  bbc_style()

finalise_plot(plot_name = engagement_trends, source = "Source: Data sourced from platform analytics reports and market research.", save_filepath = '/path/to/output/chart/chart_0001/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2018, 2018, 2019, 2019, 2019, 2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022),
  Region = c("North America", "Europe", "Asia-Pacific", "North America", "Europe", "Asia-Pacific", 
             "North America", "Europe", "Asia-Pacific", "North America", "Europe", "Asia-Pacific", 
             "North America", "Europe", "Asia-Pacific"),
  Corporate_Tax_Rate = c(21, 23, 25, 21, 25, 24, 20, 24, 26, 22, 22, 25, 21, 21, 24),
  Business_Growth_Index = c(102, 98, 105, 106, 100, 107, 99, 95, 103, 108, 97, 108, 110, 100, 109)
)

plot <- ggplot(data, aes(x = Year, y = Business_Growth_Index, color = Region, group = Region)) +
  geom_line(size = 1.5, alpha = 0.8) +
  geom_point(size = 4, aes(shape = Region)) +
  geom_text_repel(
    aes(label = Business_Growth_Index),
    size = 6,
    fontface = "bold",
    box.padding = 0.7,
    point.padding = 0.5,
    force = 25,
    force_pull = 0.2,
    segment.size = 0.4,
    segment.color = "gray50",
    min.segment.length = 0.2,
    direction = "y",
    hjust = 0.5,
    vjust = 0.5,
    max.overlaps = 20,
    show.legend = FALSE
  ) +
  scale_color_uchicago() +
  scale_shape_manual(values = c(16, 17, 18)) +
  scale_x_continuous(breaks = unique(data$Year)) +
  scale_y_continuous(breaks = seq(90, 110, 5), limits = c(90, 115)) +
  labs(
    title = "Trends in Corporate Tax Policies and Business Growth",
    subtitle = "Business growth varies with tax policy adjustments across regions (2018-2022)",
    x = "Year",
    y = "Business Growth Index",
    color = "Region",
    shape = "Region"
  ) +
  theme_ipsum_rc(
    base_size = 20,
    base_family = "Arial",
    grid = "Y"
  ) +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.margin = margin(t = 10, b = 10),
    legend.text = element_text(size = 20),
    legend.title = element_text(size = 20, face = "bold"),
    plot.title = element_text(size = 24, face = "bold"),
    plot.subtitle = element_text(size = 20),
    axis.title = element_text(size = 20, face = "bold"),
    axis.text = element_text(size = 20),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +
  theme_gdocs() +
  bbc_style()

finalise_plot(plot_name = plot, source = "Source: Data is sourced from government tax publications and economic reports.", save_filepath = '/path/to/output/chart/chart_0004/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  `Region A` = c(10, 12, 15, 18, 20),
  `Region B` = c(7, 9, 13, 10, 15),
  `Region C` = c(5, 4, 8, 12, 10)
)

data_long <- reshape2::melt(data, id.vars = "Year", variable.name = "Region", value.name = "Impact")

# Add a column for label positioning
data_long$vjust <- ifelse(data_long$Region == "Region A", -0.8,
                         ifelse(data_long$Region == "Region B", 1.5, -0.8))

# Create unique positions for the last point labels
last_year_data <- subset(data_long, Year == 2022)
last_year_data$nudge_x <- c(0.2, 0.2, 0.2)
last_year_data$nudge_y <- c(1, -1, 0.5)

grouped_bars_20250306165454 <- ggplot(data_long, aes(x = Year, y = Impact, color = Region, group = Region)) +
  geom_line(size = 1.5) +
  geom_point(size = 4, aes(shape = Region)) +
  geom_text_repel(
    data = subset(data_long, Year != 2022),
    aes(label = Impact),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 12,
    segment.size = 0.7,
    segment.color = "gray50",
    segment.alpha = 0.7,
    min.segment.length = 0,
    max.overlaps = 20,
    show.legend = FALSE
  ) +
  # Special handling for the last year to ensure labels are spread out
  geom_text_repel(
    data = last_year_data,
    aes(label = Impact, x = Year + nudge_x, y = Impact + nudge_y),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.8,
    force = 15,
    nudge_x = 0.25,
    direction = "y",
    hjust = 0,
    segment.size = 0.7,
    segment.color = "gray50",
    segment.alpha = 0.7,
    show.legend = FALSE
  ) +
  scale_x_continuous(breaks = 2018:2022, labels = 2018:2022, expand = c(0.1, 0.15)) +
  scale_y_continuous(limits = c(0, 22), breaks = seq(0, 22, 4)) +
  scale_shape_manual(values = c(16, 17, 15)) +
  scale_color_brewer(palette = "Dark2") +
  labs(
    title = "Impact of Misinformation Campaigns on Public Health Policies",
    subtitle = "Data shows variations in misinformation impact across regions over time",
    x = "Year",
    y = "Impact Score"
  ) +
  guides(
    color = guide_legend(title = "Region", override.aes = list(size = 6)),
    shape = guide_legend(title = "Region", override.aes = list(size = 6))
  ) +
  theme_wsj() +
  theme(
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 20)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title = element_text(size = 20, face = "bold"),
    axis.text = element_text(size = 20),
    legend.title = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 20),
    legend.position = "bottom",
    legend.box = "horizontal",
    legend.margin = margin(t = 20),
    legend.key.size = unit(1.5, "cm"),
    legend.spacing.x = unit(1, "cm"),
    plot.margin = margin(20, 20, 20, 20)
  ) + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Derived from public health reports, academic studies, and governmental policy reviews.", save_filepath = '/path/to/output/chart/chart_0010/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2019, 2020, 2021, 2022, 2023),
  Tech = c(25, 55, 70, 75, 80),
  Finance = c(15, 30, 40, 45, 50),
  Healthcare = c(5, 10, 12, 15, 18)
)

data_long <- tidyr::pivot_longer(data, cols = -Year, names_to = "Industry", values_to = "RemoteWorkPercentage")

# Set custom color palette
industry_colors <- c("Tech" = "#0072B2", "Finance" = "#E69F00", "Healthcare" = "#CC79A7")

# Create plot with optimized aesthetics
trend_line_plot <- ggplot(data_long, aes(x = Year, y = RemoteWorkPercentage, color = Industry, group = Industry)) +
  geom_line(size = 1.8, alpha = 0.9) +
  geom_point(size = 5, aes(shape = Industry), fill = "white", stroke = 1.5) +
  geom_text_repel(
    aes(label = paste0(RemoteWorkPercentage, "%")),
    size = 6,
    fontface = "bold",
    box.padding = 1,
    point.padding = 0.8,
    force = 30,
    segment.size = 0.6,
    segment.color = "gray50",
    min.segment.length = 0.2,
    max.overlaps = 15,
    nudge_x = 0.05,
    direction = "y",
    show.legend = FALSE
  ) +
  scale_color_manual(values = industry_colors) +
  scale_shape_manual(values = c(21, 22, 23)) +
  scale_x_continuous(breaks = 2019:2023, labels = 2019:2023) +
  scale_y_continuous(limits = c(0, 90), breaks = seq(0, 90, by = 10)) +
  labs(title = "Trends in Remote Work Adoption by Industry",
       subtitle = "Tech, Finance, and Healthcare show varied remote work adoption trends (2019-2023)",
       x = "Year", 
       y = "Remote Work Percentage (%)",
       color = "Industry",
       shape = "Industry") +
  theme_ipsum_rc(base_size = 20, base_family = "Helvetica") +
  theme(
    legend.position = "top",
    legend.box = "horizontal",
    legend.margin = margin(t = 10, b = 10),
    legend.key.size = unit(1.5, "cm"),
    legend.text = element_text(size = 22),
    legend.title = element_text(size = 24, face = "bold"),
    axis.text = element_text(size = 20, face = "bold"),
    axis.title = element_text(size = 22, face = "bold"),
    plot.title = element_text(size = 28, face = "bold"),
    plot.subtitle = element_text(size = 22),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank()
  ) +
  guides(color = guide_legend(override.aes = list(size = 8), nrow = 1, byrow = TRUE)) +
  bbc_style()

finalise_plot(plot_name = trend_line_plot, source = "Source: Data sourced from industry surveys by leading consulting firms and tech research companies.", save_filepath = '/path/to/output/chart/chart_0011/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  Christians = c(150, 170, 160, 180, 175),
  Muslims = c(230, 240, 210, 220, 250),
  Jews = c(190, 220, 200, 215, 210)
)

data_long <- reshape2::melt(data, id.vars = "Year", variable.name = "Religion", value.name = "Count")

line_chart <- ggplot(data_long, aes(x = Year, y = Count, color = Religion)) +
  geom_line(size = 1.8, alpha = 0.9) +
  geom_point(size = 5, aes(shape = Religion)) +
  scale_shape_manual(values = c(19, 17, 15)) +
  ggrepel::geom_text_repel(
    aes(label = Count),
    size = 7,
    fontface = "bold",
    box.padding = 1.2,
    point.padding = 1.2,
    force = 20,
    max.overlaps = 10,
    segment.size = 0.7,
    segment.color = "gray40",
    min.segment.length = 0.2,
    direction = "y",
  
    show.legend = FALSE
  ) +
  scale_x_continuous(breaks = c(2018, 2019, 2020, 2021, 2022)) +
  scale_y_continuous(limits = c(140, 260), breaks = seq(140, 260, 20)) +
  labs(
    title = "Hate Crimes Against Religious Communities",
    subtitle = "Analysis reveals diverse trends in hate crimes against three major religious groups.",
    x = "Year",
    y = "Number of Hate Crimes"
  ) +
  theme_ipsum_rc(grid = "Y", base_size = 20) +
  theme(
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title.x = element_text(size = 22, margin = margin(t = 15)),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.text = element_text(size = 20, face = "bold"),
    legend.title = element_text(size = 22),
    legend.text = element_text(size = 20),
    legend.position = "top",
    legend.direction = "horizontal",
    legend.spacing.x = unit(1, "cm"),
    legend.margin = margin(t = 10, b = 10),
    plot.margin = margin(t = 20, r = 30, b = 20, l = 20)
  ) +
  scale_color_jama() +
  theme_wsj() +
  bbc_style()

finalise_plot(plot_name = line_chart, source = "Sourse: Data compiled from government crime reports, human rights organizations, and academic research studies.", save_filepath = '/path/to/output/chart/chart_0016/chart.png', width_pixels = 950, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2021, 2021, 2021, 2021, 2022),
  Quarter = c("Q1", "Q2", "Q3", "Q4", "Q1"),
  Event = c("A", "A", "A", "A", "A"),
  Awareness = c(70, 72, 75, 77, 80),
  OpinionPositive = c(50, 55, 58, 60, 65),
  MisinformationInstances = c(15, 18, 14, 12, 10)
)

dataB <- data.frame(
  Year = c(2021, 2021, 2021, 2021, 2022),
  Quarter = c("Q1", "Q2", "Q3", "Q4", "Q1"),
  Event = c("B", "B", "B", "B", "B"),
  Awareness = c(65, 62, 68, 70, 75),
  OpinionPositive = c(40, 38, 41, 43, 47),
  MisinformationInstances = c(20, 22, 25, 27, 30)
)

dataC <- data.frame(
  Year = c(2021, 2021, 2021, 2021, 2022),
  Quarter = c("Q1", "Q2", "Q3", "Q4", "Q1"),
  Event = c("C", "C", "C", "C", "C"),
  Awareness = c(58, 60, 63, 67, 70),
  OpinionPositive = c(45, 42, 47, 49, 52),
  MisinformationInstances = c(18, 17, 19, 21, 23)
)

combined_data <- rbind(data, dataB, dataC)

combined_data$Quarter <- factor(combined_data$Quarter, levels = c("Q1", "Q2", "Q3", "Q4"))
combined_data$Period <- paste(combined_data$Year, combined_data$Quarter)
combined_data$Period <- factor(combined_data$Period, levels = unique(combined_data$Period))
combined_data$Event <- factor(combined_data$Event, levels = c("A", "B", "C"))

# Custom color palette
event_colors <- c("A" = "#1F77B4", "B" = "#FF7F0E", "C" = "#2CA02C")

awareness_plot <- ggplot(combined_data, aes(x = Period, y = Awareness, color = Event, group = Event)) +
  geom_line(size = 1.5) +
  geom_point(size = 4, aes(shape = Event)) +
  geom_text_repel(
    aes(label = Awareness), 
    size = 6,
    fontface = "bold",
    box.padding = 0.8, 
    point.padding = 0.5,
    force = 12,
    nudge_y = 1.5,
    min.segment.length = 0,
    segment.size = 0.7,
    segment.color = "gray50",
    direction = "y",
    show.legend = FALSE
  ) +
  labs(
    title = "Impact of Viral Content on Public Perception",
    subtitle = "Awareness Level Trends by Event (2021-2022)",
    y = "Awareness (%)",
    x = ""
  ) +
  scale_y_continuous(limits = c(55, 85), breaks = seq(55, 85, 5)) +
  scale_color_manual(values = event_colors, name = "Event Type") +
  scale_shape_manual(values = c(16, 17, 15), name = "Event Type") +
  theme_ipsum_rc(grid = "Y", base_size = 20) +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.spacing.x = unit(1, "cm"),
    legend.title = element_text(size = 22, face = "bold"),
    legend.text = element_text(size = 20),
    plot.title = element_text(size = 24, face = "bold"),
    plot.subtitle = element_text(size = 20),
    axis.title.y = element_text(size = 20, face = "bold", margin = margin(r = 15)),
    axis.text.x = element_text(size = 20, angle = 0),
    axis.text.y = element_text(size = 20)
  )

opinion_plot <- ggplot(combined_data, aes(x = Period, y = OpinionPositive, color = Event, group = Event)) +
  geom_line(size = 1.5) +
  geom_point(size = 4, aes(shape = Event)) +
  geom_text_repel(
    aes(label = OpinionPositive), 
    size = 6,
    fontface = "bold",
    box.padding = 0.8, 
    point.padding = 0.5,
    force = 12,
    nudge_y = 1.5,
    min.segment.length = 0,
    segment.size = 0.7,
    segment.color = "gray50",
    direction = "y",
    show.legend = FALSE
  ) +
  labs(
    subtitle = "Positive Opinion Trends by Event (2021-2022)",
    y = "Positive Opinion (%)",
    x = ""
  ) +
  scale_y_continuous(limits = c(35, 70), breaks = seq(35, 70, 5)) +
  scale_color_manual(values = event_colors, name = "Event Type") +
  scale_shape_manual(values = c(16, 17, 15), name = "Event Type") +
  theme_ipsum_rc(grid = "Y", base_size = 20) +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.spacing.x = unit(1, "cm"),
    legend.title = element_text(size = 22, face = "bold"),
    legend.text = element_text(size = 20),
    plot.subtitle = element_text(size = 20),
    axis.title.y = element_text(size = 20, face = "bold", margin = margin(r = 15)),
    axis.text.x = element_text(size = 20, angle = 0),
    axis.text.y = element_text(size = 20)
  )

misinformation_plot <- ggplot(combined_data, aes(x = Period, y = MisinformationInstances, color = Event, group = Event)) +
  geom_line(size = 1.5) +
  geom_point(size = 4, aes(shape = Event)) +
  geom_text_repel(
    aes(label = MisinformationInstances), 
    size = 6,
    fontface = "bold",
    box.padding = 0.8, 
    point.padding = 0.5,
    force = 12,
    nudge_y = 1.5,
    min.segment.length = 0,
    segment.size = 0.7,
    segment.color = "gray50",
    direction = "y",
    show.legend = FALSE
  ) +
  labs(
    subtitle = "Misinformation Instances by Event (2021-2022)",
    y = "Misinformation Instances",
    x = "Time Period"
  ) +
  scale_y_continuous(limits = c(5, 35), breaks = seq(5, 35, 5)) +
  scale_color_manual(values = event_colors, name = "Event Type") +
  scale_shape_manual(values = c(16, 17, 15), name = "Event Type") +
  theme_ipsum_rc(grid = "Y", base_size = 20) +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.spacing.x = unit(1, "cm"),
    legend.title = element_text(size = 22, face = "bold"),
    legend.text = element_text(size = 20),
    plot.subtitle = element_text(size = 20),
    axis.title.y = element_text(size = 20, face = "bold", margin = margin(r = 15)),
    axis.title.x = element_text(size = 20, face = "bold", margin = margin(t = 15)),
    axis.text.x = element_text(size = 20, angle = 0),
    axis.text.y = element_text(size = 20)
  )

# Combine all three plots
library(patchwork)
grouped_bars_20250306165454 <- (awareness_plot / opinion_plot / misinformation_plot) +
  plot_layout(guides = "collect") +
  plot_annotation(
    title = "Impact of Viral Content on Public Perception of Global Events",
    subtitle = "Viral content influences event awareness, opinions, and misinformation trends (2021-2022)",
    theme = theme(
      plot.title = element_text(size = 24, face = "bold", hjust = 0.5),
      plot.subtitle = element_text(size = 20, hjust = 0.5),
      legend.position = "top"
    )
  ) + theme_economist() + bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Source: Data sourced from media reports, social media analytics, and academic research studies.", save_filepath = '/path/to/output/chart/chart_0031/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)
library(hrbrthemes)

data <- data.frame(
  Year = c(2015, 2016, 2017, 2018, 2019, 2020),
  Christianity = c(25, 27, 29, 30, 28, 26),
  Islam = c(30, 32, 28, 29, 31, 33),
  Buddhism = c(15, 16, 17, 18, 19, 20)
)

data_long <- reshape2::melt(data, id.vars = "Year", variable.name = "Religion", value.name = "Participation")

# Add a column for label positioning
data_long$vjust <- ifelse(data_long$Religion == "Buddhism", 1.5, 
                         ifelse(data_long$Religion == "Christianity", -0.5, 0.5))

line_plot <- ggplot(data_long, aes(x = Year, y = Participation, color = Religion, group = Religion)) +
  geom_line(size = 1.5) +
  geom_point(size = 4, alpha = 0.9) +
  geom_text_repel(
    aes(label = paste0(Participation, "%")),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 20,
    segment.size = 0.7,
    segment.color = "gray50",
    min.segment.length = 0.3,
   
    show.legend = FALSE
  ) +
  scale_color_npg() +
  scale_x_continuous(breaks = data$Year) +
  scale_y_continuous(limits = c(10, 38), breaks = seq(10, 35, by = 5)) +
  labs(
    title = "Youth Participation in Religious Organizations",
    subtitle = "Trends observed across major religions (2015-2020)",
    x = "Year",
    y = "Participation (%)",
    color = "Religion"
  ) +
  theme_few() +
  theme(
    text = element_text(size = 20, family = "sans"),
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title = element_text(size = 20, face = "bold"),
    axis.text = element_text(size = 20),
    legend.title = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 20),
    legend.position = "bottom",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.margin = margin(t = 20),
    legend.key.width = unit(2, "cm"),
    panel.grid.major = element_line(color = "gray90"),
    panel.grid.minor = element_blank(),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +
  bbc_style()

finalise_plot(plot_name = line_plot, source = "Sourse: Data is sourced from the Pew Research Center and the World Values Survey reports.", save_filepath = '/path/to/output/chart/chart_0032/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  NATO = c(75, 78, 80, 82, 84),
  SCO = c(60, 62, 65, 63, 67),
  AU = c(45, 47, 50, 52, 53)
)

data_long <- reshape2::melt(data, id.vars = "Year", variable.name = "Organization", value.name = "Index")

# Create positions for label placement to reduce overlap
data_long$label_y <- data_long$Index
data_long$hjust <- 0.5
data_long$vjust <- -0.8

# Last points with more offset for better visibility
last_points <- subset(data_long, Year == 2022)
data_long$nudge_x <- ifelse(data_long$Year == 2022, 0.2, 0)
data_long$nudge_y <- ifelse(data_long$Year == 2022, c(2, -2, 2), 0)

line_chart <- ggplot(data_long, aes(x = Year, y = Index, color = Organization, group = Organization)) +
  geom_line(size = 1.8) +
  geom_point(size = 5, alpha = 0.9) +
  geom_text_repel(
    aes(label = Index, y = label_y),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    nudge_x = data_long$nudge_x,
    nudge_y = data_long$nudge_y,
    segment.size = 0.5,
    segment.color = "gray50",
    min.segment.length = 0.1,
    max.overlaps = 20,
    show.legend = FALSE
  ) +
  scale_color_aaas(name = "Organization") +
  scale_x_continuous(breaks = 2018:2022, limits = c(2017.5, 2022.7)) +
  scale_y_continuous(limits = c(40, 90), breaks = seq(40, 90, by = 10)) +
  labs(
    title = "Impact of Regional Conflicts on Security Frameworks",
    subtitle = "Regional conflicts caused shifts in security alliances and protocols.",
    x = "Year",
    y = "Security Index"
  ) +
  theme_ipsum_rc(base_size = 20, base_family = "Helvetica") +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.title = element_text(size = 22, face = "bold"),
    legend.text = element_text(size = 20),
    legend.key.size = unit(1.5, "cm"),
    legend.spacing.x = unit(0.5, "cm"),
    plot.title = element_text(size = 24, face = "bold"),
    plot.subtitle = element_text(size = 20),
    axis.title = element_text(size = 22, face = "bold"),
    axis.text = element_text(size = 20),
    panel.grid.minor = element_blank()
  ) +
  theme_calc() +
  bbc_style()

finalise_plot(plot_name = line_chart, source = "Source: Data sourced from international security organizations' annual reports and conflict monitoring databases.", save_filepath = '/path/to/output/chart/chart_0043/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)
library(reshape2)

data <- data.frame(
    Month = c("Jan", "Feb", "Mar", "Apr", "May", "Jun"),
    Politics = c(60, 63, 58, 65, 62, 66),
    Economy = c(55, 57, 60, 58, 61, 63),
    Health = c(65, 64, 68, 66, 67, 69)
)

data_long <- melt(data, id.vars = "Month", variable.name = "Category", value.name = "OpinionScore")

# Set Month as a factor with correct order
data_long$Month <- factor(data_long$Month, levels = c("Jan", "Feb", "Mar", "Apr", "May", "Jun"))

dynamic_lines <- ggplot(data_long, aes(x = Month, y = OpinionScore, color = Category, group = Category)) +
  geom_line(size = 1.5) +
  geom_point(size = 4, aes(shape = Category)) +
  geom_text_repel(
    aes(label = OpinionScore),
    size = 6,               
    fontface = "bold",      
    box.padding = 0.8,       
    point.padding = 0.8,     
    force = 25,             
    nudge_y = 1,
    segment.size = 0.4,
    segment.color = "gray50", 
    min.segment.length = 0.3, 
    direction = "y",
    max.overlaps = 20,
    show.legend = FALSE
  ) +
  labs(
    title = "Impact of Real-Time News on Public Opinion Dynamics",
    subtitle = "Different news topics show varied influence patterns on public opinion.",
    x = "",
    y = "Opinion Score",
    color = "Topic Category",
    shape = "Topic Category"
  ) +
  scale_y_continuous(limits = c(50, 75), breaks = seq(50, 75, 5)) +
  scale_shape_manual(values = c(16, 17, 18)) +
  guides(
    color = guide_legend(title.position = "top", ncol = 3, byrow = TRUE),
    shape = guide_legend(title.position = "top", ncol = 3, byrow = TRUE)
  ) +
  theme_minimal(base_size = 20) +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.margin = margin(t = 10, b = 10),
    legend.text = element_text(size = 20),
    legend.title = element_text(size = 20, face = "bold"),
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 10)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title = element_text(size = 20, face = "bold"),
    axis.text = element_text(size = 20),
    axis.text.x = element_text(angle = 0, hjust = 0.5),
    panel.grid.minor = element_blank()
  ) +
  scale_color_manual(values = pal_simpsons()(3)) +
  theme_stata() + 
  bbc_style()

finalise_plot(plot_name = dynamic_lines, source = "Sourse: Based on surveys and sentiment analysis from media impact research firms.", save_filepath = '/path/to/output/chart/chart_0046/chart.png', width_pixels = 896, height_pixels = 630)
"""
]

Single_broken_line_dotted = [
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

# Create the data frame
data <- data.frame(
  Age.Group = c("15-24", "25-34", "35-44", "45-54", "55+"),
  Hours.Per.Day = c(4.5, 4.0, 3.5, 3.0, 2.5)
)

# Create labels for points
data$label <- sprintf("%.1f", data$Hours.Per.Day)

# Create the plot
broken_line_chart <- ggplot(data, aes(x = Age.Group, y = Hours.Per.Day)) +
  geom_line(linetype = "dashed", size = 1.5, color = "#3182bd", group = 1) +
  geom_point(size = 5, color = "#e6550d", alpha = 0.9) +
  geom_text_repel(
    aes(label = label),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 12,
    force_pull = 0.1,
    segment.size = 0.5,
    segment.color = "gray50",
    min.segment.length = 0.1,
    direction = "y",
    nudge_y = 0.3,
    show.legend = FALSE
  ) +
  scale_y_continuous(limits = c(0, 5.5), breaks = seq(0, 5, 1)) +
  labs(
    title = "Digital Media Consumption by Age Group",
    subtitle = "Younger age groups consume more digital media than older groups",
    x = "",
    y = "Hours Per Day"
  ) +
  theme_minimal(base_size = 20) +
  theme(
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 10)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title.y = element_text(size = 20, margin = margin(r = 10)),
    axis.text = element_text(size = 20, face = "bold"),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank(),
    legend.position = "none"
  ) +
  theme_gdocs() +
  bbc_style()

finalise_plot(plot_name = broken_line_chart, source = "Sourse: Data sourced from Pew Research Center and Nielsen surveys.", save_filepath = '/path/to/output/chart/chart_0015/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(Year = c(2018, 2019, 2020, 2021, 2022),
                   Worldwide_Listeners_millions = c(200, 230, 275, 320, 370))

consumption_trend <- ggplot(data, aes(x = Year, y = Worldwide_Listeners_millions)) +
  geom_line(linetype = "dashed", color = "#3366CC", size = 1.5) +
  geom_point(size = 5, color = "#3366CC", fill = "white", shape = 21, stroke = 2) +
  geom_text_repel(
    aes(label = paste0(Worldwide_Listeners_millions, "M")),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.7,
    force = 12,
    force_pull = 0.2,
    segment.size = 0.7,
    segment.color = "gray40",
    min.segment.length = 0.2,
    direction = "y",
    hjust = 0.5,
    nudge_y = 15
  ) +
  scale_y_continuous(limits = c(150, 450), breaks = seq(150, 450, 50)) +
  scale_x_continuous(breaks = c(2018, 2019, 2020, 2021, 2022)) +
  labs(title = "Global Podcast Consumption Trends",
       subtitle = "Worldwide listeners (millions) from 2018-2022",
       x = "",
       y = "Worldwide Listeners (Millions)") +
  theme_economist() +
  theme(
    text = element_text(family = "sans", size = 20),
    plot.title = element_text(size = 24, face = "bold"),
    plot.subtitle = element_text(size = 20),
    axis.title.y = element_text(size = 20, margin = margin(r = 15)),
    axis.text = element_text(size = 20),
    legend.position = "none",
    panel.grid.major.y = element_line(color = "gray90", size = 0.5),
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  bbc_style()

finalise_plot(plot_name = consumption_trend, source = "Source: Data sourced from Edison Research and the Podcast Consumer Tracking Report.", save_filepath = '/path/to/output/chart/chart_0020/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020),
  Projects = c(150, 160, 170, 180, 185, 190, 210, 220, 240, 250, 260)
)

collaboration_trend <- ggplot(data, aes(x = Year, y = Projects)) +
  geom_line(linetype = "dashed", size = 1.5, color = "#4285F4") +
  geom_point(color = "#EA4335", size = 4.5, alpha = 0.9) +
  geom_text_repel(
    aes(label = Projects),
    size = 6, 
    fontface = "bold", 
    box.padding = 0.8, 
    point.padding = 0.7, 
    force = 15, 
    force_pull = 0.2, 
    segment.size = 0.5, 
    segment.color = "gray40", 
    min.segment.length = 0.3, 
    direction = "both", 
    nudge_y = 5,
    show.legend = FALSE
  ) +
  labs(
    title = "Trends in International Scientific Collaboration", 
    subtitle = "Increased collaboration observed post-2015.",
    y = "Number of Projects",
    x = "Year"
  ) +
  scale_y_continuous(limits = c(140, 280), breaks = seq(140, 280, 20)) +
  scale_x_continuous(breaks = data$Year) +
  theme_calc() +
  theme(
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title = element_text(size = 20, face = "bold"),
    axis.text = element_text(size = 20),
    axis.text.x = element_text(angle = 45, hjust = 1),
    panel.grid.major = element_line(color = "gray90"),
    panel.grid.minor = element_blank(),
    legend.position = "top",
    legend.text = element_text(size = 20),
    legend.title = element_text(size = 20, face = "bold")
  ) + 
  bbc_style()

finalise_plot(plot_name = collaboration_trend, source = "Sourse: Data is sourced from UNESCO Science Report, Scopus, and international research institution reports.", save_filepath = '/path/to/output/chart/chart_0041/chart.png', width_pixels = 896, height_pixels = 630)
"""
]

multiple_broken_lines_dotted = [
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2018, 2019, 2019, 2020, 2020, 2021, 2021, 2022, 2022),
  City = c("City A", "City B", "City A", "City B", "City A", "City B", "City A", "City B", "City A", "City B"),
  Immigration_Rate = c(4.5, 3.2, 5.0, 3.4, 4.8, 3.5, 5.5, 3.6, 6.0, 3.7),
  Infrastructure_Index = c(75, 68, 78, 70, 80, 71, 83, 73, 87, 75)
)

# Create better presentation of year as factor
data$Year <- as.factor(data$Year)

# Create the main plot with improved aesthetics
immigration_plot <- ggplot(data, aes(x = Year)) +
  # Immigration rate lines with improved styling
  geom_line(aes(y = Immigration_Rate, color = City, group = City), 
            size = 1.5, alpha = 0.8) +
  # Immigration rate points with larger sizes
  geom_point(aes(y = Immigration_Rate, color = City, shape = City), 
             size = 4, alpha = 0.9) +
  # Labels for immigration rate with better positioning
  geom_text_repel(
    aes(y = Immigration_Rate, label = Immigration_Rate, color = City),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 15,
    force_pull = 0,
    nudge_y = 0.2,
    segment.size = 0.5,
    segment.color = "gray50",
    min.segment.length = 0,
    direction = "y",
    show.legend = FALSE
  ) +
  # Infrastructure index lines with improved styling
  geom_line(aes(y = Infrastructure_Index / 10, color = City, group = City), 
            size = 1.5, linetype = "dashed", alpha = 0.8) +
  # Infrastructure index points
  geom_point(aes(y = Infrastructure_Index / 10, color = City, shape = City), 
             size = 4, alpha = 0.9) +
  # Labels for infrastructure index with better positioning
  geom_text_repel(
    aes(y = Infrastructure_Index / 10, label = Infrastructure_Index, color = City),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 15,
    force_pull = 0,
    nudge_y = -0.3,
    segment.size = 0.5,
    segment.color = "gray50",
    min.segment.length = 0,
    direction = "y",
    show.legend = FALSE
  ) +
  # Improved color palette
  scale_color_lancet() +
  # Custom shapes
  scale_shape_manual(values = c(16, 17)) +
  # Improved axis scales
  scale_y_continuous(
    limits = c(2.5, 9.5),
    breaks = seq(3, 9, 1),
    sec.axis = sec_axis(~.*10, 
                        name = "Infrastructure Index",
                        breaks = seq(30, 90, 10))
  ) +
  # Better labels with larger font
  labs(
    title = "Impact of Immigration on Urban Infrastructure Growth",
    subtitle = "Variations in Urban Infrastructure Development Linked to Immigration Rates",
    x = "Year",
    y = "Immigration Rate (%)",
    caption = ""
  ) +
  # Improved theme with larger fonts
  theme_few() +
  theme(
    plot.title = element_text(size = 24, face = "bold", hjust = 0.5),
    plot.subtitle = element_text(size = 20, hjust = 0.5, margin = margin(b = 20)),
    axis.title.x = element_text(size = 22, margin = margin(t = 15)),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.text.x = element_text(size = 20, face = "bold"),
    axis.text.y = element_text(size = 20),
    legend.title = element_text(size = 20),
    legend.text = element_text(size = 20),
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.margin = margin(t = 10, b = 10),
    legend.spacing.x = unit(2, "cm"),
    panel.grid.major.y = element_line(color = "gray90"),
    panel.grid.minor = element_blank()
  ) +
  # Better legend
  guides(
    color = guide_legend(title = "City:", override.aes = list(size = 5)),
    shape = guide_legend(title = "City:", override.aes = list(size = 5))
  ) +
  # Add bbc style
  bbc_style()

# Save the final plot
finalise_plot(plot_name = immigration_plot, 
              source = "Sourse: Data is assumed to be sourced from government census reports, urban development agencies, and migration studies.", 
              save_filepath = '/path/to/output/chart/chart_0006/chart.png', 
              width_pixels = 896, 
              height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022, 2023),
  Privacy_Concerns_Index = c(7.2, 7.5, 8.0, 8.4, 8.6, 9.0),
  GDPR_Impact = c(5.5, 6.3, 7.0, 7.2, 7.5, 8.0),
  Legislation_Effectiveness = c(4.3, 4.8, 5.5, 6.0, 6.3, 6.8)
)

# Add nicer labels for the plot
data$Year_f <- as.factor(data$Year)

broken_lines <- ggplot(data, aes(x = Year)) +
  # Use thicker lines with different line types for better differentiation
  geom_line(aes(y = Privacy_Concerns_Index, color = "Privacy Concerns Index"), 
            linetype = "solid", size = 1.5) +
  geom_line(aes(y = GDPR_Impact, color = "GDPR Impact"), 
            linetype = "dashed", size = 1.5) +
  geom_line(aes(y = Legislation_Effectiveness, color = "Legislation Effectiveness"), 
            linetype = "dotdash", size = 1.5) +
  # Add points to highlight data positions
  geom_point(aes(y = Privacy_Concerns_Index, color = "Privacy Concerns Index"), size = 4) +
  geom_point(aes(y = GDPR_Impact, color = "GDPR Impact"), size = 4) +
  geom_point(aes(y = Legislation_Effectiveness, color = "Legislation Effectiveness"), size = 4) +
  # Improve label placement with ggrepel
  geom_text_repel(aes(y = Privacy_Concerns_Index, label = Privacy_Concerns_Index),
                  size = 5, fontface = "bold", nudge_y = 0.4, nudge_x = 0.1,
                  box.padding = 0.7, point.padding = 0.5, 
                  force = 10, segment.size = 0.6,
                  segment.color = "gray40", direction = "y") +
  geom_text_repel(aes(y = GDPR_Impact, label = GDPR_Impact),
                  size = 5, fontface = "bold", nudge_y = -0.4, nudge_x = 0.1,
                  box.padding = 0.7, point.padding = 0.5, 
                  force = 10, segment.size = 0.6,
                  segment.color = "gray40", direction = "y") +
  geom_text_repel(aes(y = Legislation_Effectiveness, label = Legislation_Effectiveness),
                  size = 5, fontface = "bold", nudge_y = 0.4, nudge_x = -0.1,
                  box.padding = 0.7, point.padding = 0.5, 
                  force = 10, segment.size = 0.6,
                  segment.color = "gray40", direction = "y") +
  # Better scale with more space to accommodate labels
  scale_y_continuous(limits = c(3, 10), breaks = seq(3, 10, 1)) +
  scale_x_continuous(breaks = unique(data$Year)) +
  # Enhanced labels and titles with larger font
  labs(title = "Online Privacy Concerns and Data Protection Policy Trends",
       subtitle = "Rise in online privacy concerns amid evolving data protection policies (2018-2023)",
       x = "Year",
       y = "Index Value (0-10 scale)",
       color = "Indicators") +
  # Better color palette 
  scale_color_nejm(name = "Indicators") +
  # Position legend for better spacing
  theme_ipsum_rc(grid = "Y", base_size = 20) +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.title = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 20),
    legend.key.size = unit(1.5, "cm"),
    legend.spacing.x = unit(1, "cm"),
    axis.title = element_text(size = 22, face = "bold"),
    axis.text = element_text(size = 20),
    plot.title = element_text(size = 24, face = "bold"),
    plot.subtitle = element_text(size = 20),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +
  # Add the required theme at the end
  theme_fivethirtyeight() +
  bbc_style()

finalise_plot(plot_name = broken_lines, 
              source = "Source: Data derived from Global Internet NGOs, GDPR Audits, and National Cybersecurity Agencies Reports.", 
              save_filepath = '/path/to/output/chart/chart_0007/chart.png', 
              width_pixels = 896, 
              height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  USA_EU = c(200, 210, 220, 225, 230),
  USA_China = c(250, 240, 230, 220, 210),
  EU_China = c(180, 190, 200, 210, 220)
)

data_melt <- reshape2::melt(data, id.vars = "Year", variable.name = "Trade_Relation", value.name = "Value")

# Update relation labels for better readability
data_melt$Trade_Relation <- factor(data_melt$Trade_Relation, 
                                   levels = c("USA_EU", "USA_China", "EU_China"),
                                   labels = c("USA-EU", "USA-China", "EU-China"))

# Create the main plot with improved aesthetics
p <- ggplot(data_melt, aes(x = Year, y = Value, color = Trade_Relation, group = Trade_Relation)) +
  geom_line(aes(linetype = Trade_Relation), size = 1.5) +
  geom_point(size = 4, aes(shape = Trade_Relation)) +
  geom_text_repel(
    aes(label = Value),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.8,
    force = 10,
    nudge_y = 5,
    segment.size = 0.6,
    segment.color = "gray40",
    min.segment.length = 0.2,
    max.overlaps = 10,
    show.legend = FALSE
  ) +
  labs(
    title = "Impact of Global Supply Chain Shifts on Trade Relations",
    subtitle = "Trade relations between USA, EU, and China (2018-2022)",
    x = "Year",
    y = "Trade Value (Billion USD)",
    color = "Trade Relation",
    linetype = "Trade Relation",
    shape = "Trade Relation"
  ) +
  scale_y_continuous(limits = c(170, 260), breaks = seq(170, 260, 20)) +
  scale_x_continuous(breaks = c(2018, 2019, 2020, 2021, 2022)) +
  scale_color_manual(values = c("USA-EU" = "#0072B2", "USA-China" = "#D55E00", "EU-China" = "#009E73")) +
  scale_linetype_manual(values = c("USA-EU" = "solid", "USA-China" = "longdash", "EU-China" = "dotdash")) +
  scale_shape_manual(values = c("USA-EU" = 16, "USA-China" = 17, "EU-China" = 15)) +
  theme_few() +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.margin = margin(t = 10, b = 10),
    legend.spacing.x = unit(1, "cm"),
    legend.title = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 20),
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 10)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    plot.caption = element_text(size = 16, hjust = 0),
    axis.title = element_text(size = 20, face = "bold"),
    axis.text = element_text(size = 20),
    panel.grid.major.y = element_line(color = "gray90"),
    panel.grid.minor = element_blank(),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +
  bbc_style()

finalise_plot(plot_name = p, source = "Source: Data is sourced from WTO and OECD trade reports, along with data from national trade departments.", save_filepath = '/path/to/output/chart/chart_0037/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = rep(2018:2022, 3),
  GDP_Growth = c(6.2, 5.9, 3.9, 5.0, 4.8, 7.9, 8.1, 3.5, 6.4, 5.6, 1.9, 2.2, -1.9, 3.4, 3.1),
  Aid = c(1.8, 2.0, 2.5, 2.3, 2.1, 0.8, 1.0, 1.5, 1.2, 1.4, 1.5, 1.6, 2.2, 1.9, 1.8),
  Country = rep(c("Kenya", "Bangladesh", "Nigeria"), each=5)
)

broken_lines <- ggplot(data, aes(x = Year, y = GDP_Growth, color = Country, linetype = Country)) +
  geom_line(size = 1.8) +
  geom_point(size = 4, aes(shape = Country)) +
  geom_text_repel(
    aes(label = GDP_Growth),
    size = 6.5,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.8,
    force = 25,
    nudge_x = 0.15,
    nudge_y = 0.3,
    segment.size = 0.7,
    segment.color = "gray50",
    min.segment.length = 0.2,
    max.overlaps = 15,
    show.legend = FALSE
  ) +
  scale_x_continuous(breaks = 2018:2022, limits = c(2017.5, 2022.5)) +
  scale_y_continuous(limits = c(-3, 9), breaks = seq(-3, 9, 2)) +
  scale_color_nejm(alpha = 0.9) +
  scale_shape_manual(values = c(16, 17, 18)) +
  scale_linetype_manual(values = c("solid", "dashed", "dotdash")) +
  theme_ipsum_rc(base_size = 20, grid = "Y") +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.spacing.x = unit(1, "cm"),
    legend.title = element_text(size = 22, face = "bold"),
    legend.text = element_text(size = 20),
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title = element_text(size = 22, face = "bold"),
    axis.text = element_text(size = 20),
    plot.margin = margin(t = 20, r = 25, b = 20, l = 20)
  ) +
  labs(
    title = "Correlation Between Foreign Aid and Economic Growth",
    subtitle = "Foreign aid shows varied impacts on GDP growth across Kenya, Bangladesh, and Nigeria",
    x = "Year",
    y = "GDP Growth (%)",
    color = "Country:",
    linetype = "Country:",
    shape = "Country:"
  ) +
  theme_solarized() +
  bbc_style()

finalise_plot(plot_name = broken_lines, source = "Source: Data is derived from World Bank and OECD reports.", save_filepath = '/path/to/output/chart/chart_0039/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  Blockchain_Adoption = c(10, 20, 35, 45, 55),
  Distribution_Cost_Savings = c(2, 5, 10, 15, 25)
)

blockchain_plot <- ggplot(data, aes(x = Year)) +
  geom_line(aes(y = Blockchain_Adoption, color = "Blockchain Adoption"), size = 1.5, linetype = "solid") +
  geom_line(aes(y = Distribution_Cost_Savings, color = "Distribution Cost Savings"), size = 1.5, linetype = "dashed") +
  geom_point(aes(y = Blockchain_Adoption, color = "Blockchain Adoption"), size = 4, shape = 19) +
  geom_point(aes(y = Distribution_Cost_Savings, color = "Distribution Cost Savings"), size = 4, shape = 17) +
  geom_text_repel(
    aes(y = Blockchain_Adoption, label = paste0(Blockchain_Adoption, "%")),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 20,
    nudge_y = 3,
    segment.size = 0.6,
    segment.color = "gray50",
    min.segment.length = 0.2,
    direction = "y",
    show.legend = FALSE
  ) +
  geom_text_repel(
    aes(y = Distribution_Cost_Savings, label = paste0(Distribution_Cost_Savings, "%")),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 20,
    nudge_y = -3,
    segment.size = 0.6,
    segment.color = "gray50",
    min.segment.length = 0.2,
    direction = "y",
    show.legend = FALSE
  ) +
  scale_color_manual(values = c("Blockchain Adoption" = "#4169E1", "Distribution Cost Savings" = "#FF4500")) +
  scale_x_continuous(breaks = data$Year) +
  scale_y_continuous(limits = c(0, 65), breaks = seq(0, 60, by = 10)) +
  labs(
    title = "Influence of Blockchain on Digital Media Distribution",
    subtitle = "Blockchain adoption increases; distribution costs decrease over 5 years",
    x = "Year",
    y = "Percentage (%)",
    color = ""
  ) +
  theme_ipsum_rc(base_size = 20, base_family = "Arial") +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5, size = 24),
    plot.subtitle = element_text(hjust = 0.5, size = 20),
    axis.title.x = element_text(size = 22, margin = margin(t = 15)),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.text = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 20),
    legend.position = "top",
    legend.box = "horizontal",
    legend.margin = margin(t = 10, b = 10),
    legend.spacing.x = unit(1, "cm"),
    panel.grid.minor = element_blank()
  ) +
  theme_stata() +
  bbc_style()

finalise_plot(plot_name = blockchain_plot, source = "Sourse: Data sourced from Gartner, PwC technology reports, and digital media industry panels.", save_filepath = '/path/to/output/chart/chart_0047/chart.png', width_pixels = 896, height_pixels = 630)
"""
]

Single_Pie_Chart = [
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

# 创建数据框
data <- data.frame(
  Entity = c("USA", "China", "Russia", "EU", "India"),
  Proportion = c(27, 24, 18, 20, 11)
)

# 计算标签位置
data <- data %>%
  arrange(desc(Entity)) %>%
  mutate(lab.ypos = cumsum(Proportion) - 0.5 * Proportion)

# 生成圆环图
grouped_donut <- ggplot(data, aes(x = 2, y = Proportion, fill = Entity)) + 
  geom_bar(stat = "identity", color = "white", width = 1) +
  coord_polar(theta = "y", start = 0) +
  geom_text(aes(y = lab.ypos, label = paste0(Proportion, "%")), color = "white") +
  scale_fill_manual(values = c("#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1")) +
  theme_void() +
  xlim(0.5, 2.5) +
  labs(
    title = "Global Influence Distribution by Major Powers",
    subtitle = "Proportion of geopolitical influence among USA, China, Russia, EU, and India"
  ) +
  theme(plot.title = element_text(size=20, face="bold"),
        plot.subtitle = element_text(size=18),
        legend.title = element_blank(),
        legend.text = element_text(size=16),
        legend.position="right")

# 保存图表
finalise_plot(plot_name = grouped_donut, 
              source = "Source: Data from United Nations databases and international relations research reports.", 
              save_filepath = '/path/to/output/chart/chart_0011/chart.png', 
              width_pixels = 800, 
              height_pixels = 630)""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

# 创建数据框
data <- data.frame(
  Entity = c("USA", "China", "Russia", "EU", "India"),
  Proportion = c(27, 24, 18, 20, 11)
)

# 设置颜色  #845ec2  #d65db1 #ff6f91 #ff9671 #ffc75f 
mycols <- c("#845ec2", "#d65db1", "#ff6f91", "#ff9671", "#ffc75f")

# 生成饼状图
grouped_bars <- ggplot(data, aes(x = "", y = Proportion, fill = Entity)) + 
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  geom_text_repel(
    aes(label = paste0(Proportion, "%")),
    position = position_stack(vjust=0.5),
    size = 6,
    fontface = "bold",
    box.padding = 0.5,
    point.padding = 0.5,
    force = 1,
    force_pull = 0.5,
    segment.size = 0.2,
    segment.color = "gray50",
    min.segment.length = 0.2,
    direction = "both",
    show.legend = FALSE
  ) +
  labs(
    title = "Global Influence Distribution by Major Powers",
    subtitle = "Proportion of geopolitical influence among USA, China, Russia, EU, and India"
  ) +
  scale_fill_manual(values = mycols) +
  theme_void() +
  theme(plot.title = element_text(size=20, face="bold"),
        plot.subtitle = element_text(size=18),
        legend.title = element_blank(),
        legend.text = element_text(size=16),
        legend.position="right")

# 保存图表
finalise_plot(plot_name = grouped_bars, 
              source = "Source: Data from United Nations databases and international relations research reports.", 
              save_filepath = '/path/to/output/chart/chart_0012/chart.png', 
              width_pixels = 800, 
              height_pixels = 630)
"""
    
]
simple_bar_chart = [
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Region = c("Region A", "Region B", "Region C", "Region D", "Region E"),
  Racial_Diversity_Index = c(75, 60, 85, 55, 95),
  Economic_Resilience_Score = c(80, 70, 90, 65, 85)
)

# Reorder regions by diversity index for better visualization
data$Region <- factor(data$Region, levels = data$Region[order(-data$Racial_Diversity_Index)])

grouped_bars_20250306165454 <- ggplot(data, aes(x = Economic_Resilience_Score, y = Region)) +
  geom_col(aes(fill = Racial_Diversity_Index), width = 0.7) +
  scale_fill_gradient(
    low = "#74add1", 
    high = "#053061",
    name = "Racial Diversity\nIndex",
    guide = guide_colorbar(
      direction = "horizontal",
      barwidth = 10,
      barheight = 1.5,
      title.position = "top",
      title.hjust = 0.5
    )
  ) +
  geom_text_repel(
    aes(label = paste0(Racial_Diversity_Index, "")),
    size = 5.5,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 15,
    nudge_x = 10,
    direction = "y",
    hjust = 0,
    segment.size = 0.7,
    segment.color = "gray30",
    min.segment.length = 0.2,
    show.legend = FALSE
  ) +
  labs(
    title = "Racial Diversity vs. Economic Resilience",
    subtitle = "Higher racial diversity often links to improved economic resilience",
    x = "Economic Resilience Score",
    y = NULL
  ) +
  scale_x_continuous(
    limits = c(0, 105),
    breaks = seq(0, 100, by = 20),
    expand = c(0, 0)
  ) +
  theme_ipsum_rc(base_size = 20) +
  theme(
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 10)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title.x = element_text(size = 20, face = "bold", margin = margin(t = 15)),
    axis.text.y = element_text(size = 20, face = "bold"),
    axis.text.x = element_text(size = 20),
    legend.title = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 18),
    legend.position = "bottom",
    legend.margin = margin(t = 20),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  theme_calc()+
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data sourced from OECD diversity indices and WEF economic resilience reports.", save_filepath = '/path/to/output/chart/chart_0008/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Category = c("Speed", "Accuracy", "Automation", "Cost Efficiency", "Personalization"),
  Impact_Percentage = c(80, 70, 65, 50, 60)
)

# Add percentage symbols to the data for display
data$label <- paste0(data$Impact_Percentage, "%")

grouped_bars_20250306165454 <- ggplot(data, aes(x = Impact_Percentage, y = reorder(Category, Impact_Percentage))) +
  geom_bar(stat = "identity", fill = pal_npg("nrc")(5), width = 0.7) +
  geom_text_repel(
    aes(label = label),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 2,
    nudge_x = 5,
    segment.size = 0.7,
    segment.color = "gray50",
    direction = "y",
    hjust = 0
  ) +
  scale_x_continuous(limits = c(0, 100), breaks = seq(0, 100, 25), labels = function(x) paste0(x, "%")) +
  labs(
    title = "Impact of AI on News Content Generation",
    subtitle = "AI significantly improves speed, accuracy, and automation",
    caption = "Higher percentage indicates stronger impact"
  ) +
  theme_ipsum_rc(base_size = 20) +
  theme(
    plot.title = element_text(face = "bold", size = 24, margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    plot.caption = element_text(size = 16, margin = margin(t = 15)),
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    axis.text.x = element_text(size = 20),
    axis.text.y = element_text(size = 20, face = "bold"),
    panel.grid.major.x = element_line(color = "gray90"),
    panel.grid.minor = element_blank(),
    panel.grid.major.y = element_blank(),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  theme_calc()+
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data based on surveys from Reuters Institute and news organizations", save_filepath = '/path/to/output/chart/chart_0019/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Impact_Factor = c("Increased Income Sources", "Skill Diversification", "Work Flexibility", "Income Variability"),
  Percentage = c(40, 25, 20, 15)
)

grouped_bars <- ggplot(data, aes(x = Percentage, y = reorder(Impact_Factor, Percentage))) +
  geom_bar(stat = "identity", fill = "#3182bd", width = 0.7) +
  geom_text_repel(
    aes(label = paste0(Percentage, "%")),
    size = 6, fontface = "bold",
    box.padding = 0.8, point.padding = 0.5,
    force = 15, force_pull = 0,
    segment.size = 0.5, segment.color = "gray50",
    min.segment.length = 0.2, direction = "y",
    nudge_x = 5, hjust = 0,
    show.legend = FALSE
  ) +
  labs(
    title = "Impact of Gig Economy on Digital Creators",
    subtitle = "Increased opportunities and income sources for digital creators due to the gig economy",
    x = "Percentage (%)",
    y = ""
  ) +
  scale_x_continuous(limits = c(0, 55), breaks = seq(0, 50, 10)) +
  theme_ipsum_rc(base_size = 20) +
  theme(
    panel.grid.minor = element_blank(),
    panel.grid.major.y = element_blank(),
    panel.grid.major.x = element_line(color = "gray85", linewidth = 0.5),
    axis.title.y = element_blank(),
    axis.title.x = element_text(size = 20, margin = margin(t = 15)),
    axis.text.y = element_text(size = 22, face = "bold", margin = margin(r = 10)),
    axis.text.x = element_text(size = 20),
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 10)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  theme_solarized() +
  bbc_style()

finalise_plot(plot_name = grouped_bars, source = "Sourse: Data collected from platform reports, industry surveys, and studies by advocacy groups.", save_filepath = '/path/to/output/chart/chart_0027/chart.png', width_pixels = 1000, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)
library(forcats)

data <- data.frame(
  Religious_Organization = c("Christianity", "Islam", "Hinduism", "Buddhism", "Judaism"),
  Youth_Participation_Percentage = c(45, 55, 40, 35, 30)
)

grouped_bars_20250306165454 <- ggplot(data, aes(x = Youth_Participation_Percentage, 
                               y = fct_reorder(Religious_Organization, Youth_Participation_Percentage))) +
  geom_col(fill = pal_npg("nrc")(5), width = 0.7) +
  geom_text_repel(
    aes(label = paste0(Youth_Participation_Percentage, "%")),
    size = 7,
    fontface = "bold",
    box.padding = 1,
    point.padding = 1,
    force = 30,
    nudge_x = 5,
    hjust = 0,
    segment.size = 0.7,
    segment.color = "gray50",
    min.segment.length = 0.2,
    direction = "y",
    show.legend = FALSE
  ) +
  scale_x_continuous(limits = c(0, 75), breaks = seq(0, 70, 10)) +
  labs(
    x = "Youth Participation (%)",
    y = "",
    title = "Youth Participation in Religious Organizations",
    subtitle = "Youth participation varies by religious denomination"
  ) +
  theme_ipsum_rc(base_size = 20, axis_title_size = 22, plot_title_size = 24, subtitle_size = 22) +
  theme(
    axis.text.y = element_text(size = 20, face = "bold"),
    axis.text.x = element_text(size = 20),
    plot.margin = margin(20, 40, 20, 20),
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank()
  ) +
  theme_excel() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, 
              source = "Sourse: Data is derived from Pew Research Center surveys and religious community reports.", 
              save_filepath = '/path/to/output/chart/chart_0030/chart.png', 
              width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Education_Level = c("High School", "Bachelor's Degree", "Master's Degree", "PhD"),
  Wage_Growth = c(10, 25, 35, 40)
)

# Create custom color palette
custom_colors <- c("#2C3E50", "#E74C3C", "#3498DB", "#1ABC9C")

grouped_bars_20250306165454 <- ggplot(data, aes(x = reorder(Education_Level, Wage_Growth), 
                                        y = Wage_Growth,
                                        fill = reorder(Education_Level, Wage_Growth))) +
  geom_bar(stat = "identity", width = 0.7) +
  scale_fill_manual(values = custom_colors) +
  coord_flip() +
  geom_text_repel(
    aes(label = paste0(Wage_Growth, "%")),
    size = 7,
    fontface = "bold",
    color = "#2C3E50",
    box.padding = 0.5,
    point.padding = 0.5,
    force = 25,
    nudge_x = 0.01,
    direction = "y",
    hjust = 0,
    segment.size = 0.7,
    segment.color = "gray50",
    min.segment.length = 0.1,
    show.legend = FALSE
  ) +
  labs(
    title = "Impact of Education Levels on Wage Growth", 
    subtitle = "Higher education levels correlate with greater wage growth.",
    x = NULL, 
    y = "Wage Growth (%)",
    caption = ""
  ) +
  scale_y_continuous(limits = c(0, 50), breaks = seq(0, 50, by = 10)) +
  theme_ipsum_rc(base_size = 22, base_family = "Helvetica") +
  theme(
    plot.title = element_text(size = 28, face = "bold", margin = margin(b = 20)),
    plot.subtitle = element_text(size = 22, margin = margin(b = 20)),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.title.x = element_text(size = 22, margin = margin(t = 15)),
    axis.text = element_text(size = 22, face = "bold"),
    legend.position = "none",
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_line(color = "gray90", linetype = "dashed"),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  theme_gdocs() +
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, 
              source = "Sourse: Data compiled from labor statistics reports and economic research publications.", 
              save_filepath = '/path/to/output/chart/chart_0034/chart.png', 
              width_pixels = 896, 
              height_pixels = 630)
"""
]
paired_bar_chart = [
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  AgeGroup = c("50-59", "60-69", "70-79", "80+"),
  Grandfathers = c(40, 60, 35, 10),
  Grandmothers = c(35, 50, 45, 15)
)

# Convert to long format for ggplot
data_long <- reshape2::melt(data, id.vars = "AgeGroup", variable.name = "Gender", value.name = "Count")

# Create a custom order for the age groups (oldest to youngest)
data_long$AgeGroup <- factor(data_long$AgeGroup, levels = c("80+", "70-79", "60-69", "50-59"))

# Create the main plot
grouped_bars_20250306165454 <- ggplot(data_long, aes(x = AgeGroup, y = Count, fill = Gender)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  geom_text(aes(label = Count, group = Gender),
            position = position_dodge(width = 0.8),
            hjust = -0.3, size = 6, fontface = "bold") +
  coord_flip() +
  scale_fill_aaas(name = "Primary Caregiver") +
  scale_y_continuous(limits = c(0, 70), expand = c(0, 0)) +
  labs(
    title = "Grandparents as Primary Caregivers by Age and Gender",
    subtitle = "More grandfathers are primary caregivers in 60-70 age range.",
    x = "Age Group",
    y = "Number of Caregivers"
  ) +
  theme_ipsum_rc(base_size = 20) +
  theme(
    legend.position = "top",
    legend.title = element_text(size = 22, face = "bold"),
    legend.text = element_text(size = 20),
    plot.title = element_text(size = 24, face = "bold"),
    plot.subtitle = element_text(size = 22),
    axis.title = element_text(size = 22, face = "bold"),
    axis.text = element_text(size = 20, face = "bold")
  ) +
  theme_gdocs() +
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data sourced from national social service reports and family caregiving studies.", save_filepath = '/path/to/output/chart/chart_0001/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
    Year = c("2018", "2019", "2020", "2021", "2022"),
    Replicated = c(45, 50, 55, 60, 58),
    Not_Replicated = c(70, 65, 60, 55, 57)
)

data_long <- reshape2::melt(data, id.vars = "Year")

# Add position columns for better label placement
data_long$position <- with(data_long, 
                           ifelse(variable == "Replicated", 
                                 value/2, 
                                 value + 5))

# Reorder years to show chronological order when flipped
data_long$Year <- factor(data_long$Year, levels = rev(c("2018", "2019", "2020", "2021", "2022")))

# Create nicer label names
data_long$variable <- factor(data_long$variable, 
                            levels = c("Replicated", "Not_Replicated"),
                            labels = c("Replicated", "Not Replicated"))

grouped_bars_20250306165454 <- ggplot(data_long, aes(x = Year, y = value, fill = variable)) + 
  geom_bar(stat = "identity", position = position_dodge(width = 0.7), width = 0.6) +
  coord_flip() +
  scale_fill_jco(alpha = 0.9) +
  labs(title = "Patterns in Replication Crisis in Psychology Research", 
       subtitle = "Comparison of replicated vs. non-replicated studies over recent years",
       x = "Year",
       y = "Number of Studies",
       fill = "Study Outcome") +
  geom_text(
    aes(label = value, y = value + ifelse(variable == "Replicated", -5, 5)),
    position = position_dodge(width = 0.7),
    size = 6,
    fontface = "bold",
    vjust = 0.5,
    show.legend = FALSE
  ) +
  scale_y_continuous(limits = c(0, 85), breaks = seq(0, 80, by = 20), expand = c(0, 0)) +
  theme_ipsum_rc(base_size = 20) + 
  theme(
    legend.position = "bottom",
    legend.title = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 20),
    legend.key.size = unit(1.5, "cm"),
    axis.title = element_text(size = 22, face = "bold"),
    plot.title = element_text(size = 26, face = "bold"),
    plot.subtitle = element_text(size = 22),
    panel.grid.minor = element_blank(),
    panel.grid.major.y = element_blank()
  ) +
  theme_calc() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data is compiled from PsycINFO, PubMed, and various meta-analyses on psychology research.", save_filepath = '/path/to/output/chart/chart_0007/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

# Data preparation
data <- data.frame(
  Region = c("Region A", "Region B", "Region C", "Region D", "Region E"),
  Rural = c(25, 15, 40, 30, 20),
  Urban = c(75, 85, 60, 70, 80)
)

# Convert to long format for ggplot
data_melt <- reshape2::melt(data, id.vars = "Region", variable.name = "Area", value.name = "Percentage")

# Reorder regions by Rural percentage (descending)
data_melt$Region <- factor(data_melt$Region, 
                           levels = data$Region[order(data$Rural, decreasing = TRUE)])

# Create plot
grouped_bars_20250306165454 <- ggplot(data_melt, aes(x = Percentage, y = Region, fill = Area)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.9), width = 0.8) +
  geom_text(aes(label = paste0(Percentage, "%")),
            position = position_dodge(width = 0.9),
            hjust = -0.3,
            size = 6,
            fontface = "bold") +
  scale_fill_npg(alpha = 0.9) +
  scale_x_continuous(limits = c(0, 105), expand = c(0, 0)) +
  labs(
    title = "Immigrant Population Distribution: Rural vs Urban",
    subtitle = "Immigrant concentration is higher in urban areas across all regions",
    x = "Percentage (%)",
    y = NULL,
    fill = "Area Type"
  ) +
  theme_ipsum_rc(base_size = 20, grid = "X") +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.justification = "center",
    legend.box.spacing = unit(1, "cm"),
    legend.margin = margin(t = 0, r = 10, b = 10, l = 10),
    legend.text = element_text(size = 20),
    legend.title = element_text(size = 22, face = "bold"),
    axis.title.x = element_text(size = 22, face = "bold", margin = margin(t = 15)),
    axis.text.y = element_text(size = 20, face = "bold"),
    axis.text.x = element_text(size = 20),
    plot.title = element_text(size = 24, face = "bold"),
    plot.subtitle = element_text(size = 20),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  theme_igray() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, 
              source = "Sourse: Data is sourced from national statistics bureaus and UNDESA reports.", 
              save_filepath = '/path/to/output/chart/chart_0016/chart.png', 
              width_pixels = 896, 
              height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Religion = c("Christianity", "Islam", "Hinduism", "Buddhism"),
  Positive = c(55, 40, 53, 70),
  Negative = c(45, 60, 47, 30)
)

# Create factor with custom order to control display order
data$Religion <- factor(data$Religion, levels = c("Buddhism", "Hinduism", "Christianity", "Islam"))

grouped_bars <- ggplot() +
  geom_bar(data = data, aes(x = Religion, y = Positive), 
           stat = "identity", position = "dodge", 
           fill = "#57B0E5", width = 0.6, alpha = 0.9) +
  geom_bar(data = data, aes(x = Religion, y = -Negative), 
           stat = "identity", position = "dodge", 
           fill = "#F27E7E", width = 0.6, alpha = 0.9) +
  coord_flip() +
  geom_text_repel(
    data = data,
    aes(x = Religion, y = Positive, label = paste0(Positive, "%")),
    size = 7,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    nudge_y = 10,
    segment.size = 0.6,
    segment.color = "gray40",
    min.segment.length = 0.1,
    direction = "y",
    show.legend = FALSE
  ) +
  geom_text_repel(
    data = data,
    aes(x = Religion, y = -Negative, label = paste0(Negative, "%")),
    size = 7,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    nudge_y = -10,
    segment.size = 0.6,
    segment.color = "gray40",
    min.segment.length = 0.1,
    direction = "y",
    show.legend = FALSE
  ) +
  labs(
    title = "Media Portrayal Patterns of Religious Groups",
    subtitle = "Positive vs. Negative Media Coverage (%)",
    x = "",
    y = ""
  ) +
  scale_y_continuous(
    limits = c(-80, 80),
    breaks = seq(-60, 60, 20),
    labels = function(x) paste0(abs(x), "%")
  ) +
  annotate("text", x = 0.5, y = 50, label = "Positive Coverage", 
           size = 6, fontface = "bold", color = "#2980B9") +
  annotate("text", x = 0.5, y = -50, label = "Negative Coverage", 
           size = 6, fontface = "bold", color = "#E74C3C") +
  theme_igray() +
  theme(
    plot.title = element_text(face = "bold", size = 24, margin = margin(b = 10)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.text.y = element_text(size = 20, face = "bold"),
    axis.text.x = element_text(size = 20),
    legend.position = "none",
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_line(color = "gray90", linetype = "dashed"),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +
  bbc_style()

finalise_plot(plot_name = grouped_bars, source = "Sourse: Data sourced from media analysis reports by media watch organizations and academic studies.", save_filepath = '/path/to/output/chart/chart_0021/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Region = c("North America", "Europe", "Asia", "Africa", "South America"),
  Research_Projects = c(150, 130, 190, 80, 100),
  Conservation_Initiatives = c(120, 160, 110, 150, 140)
)

# Reorder regions by total value
data$Region <- factor(data$Region, 
                     levels = data$Region[order(data$Research_Projects + data$Conservation_Initiatives)])

# Convert to long format for ggplot
data_long <- reshape2::melt(data, id.vars = "Region")

# Improve variable names for legend
data_long$variable <- factor(data_long$variable,
                            levels = c("Research_Projects", "Conservation_Initiatives"),
                            labels = c("Research Projects", "Conservation Initiatives"))

# Create improved plot
grouped_bars <- ggplot(data_long, aes(x = Region, y = value, fill = variable)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  coord_flip() +
  scale_fill_manual(values = c("#3182BD", "#31A354")) +
  scale_y_continuous(limits = c(0, 220), breaks = seq(0, 200, 50), expand = c(0, 10)) +
  labs(
    title = "Global Biodiversity Research and Conservation Initiatives",
    subtitle = "Notable regional differences in research and conservation efforts",
    x = "",
    y = "Count",
    fill = ""
  ) +
  geom_text(
    aes(label = value),
    position = position_dodge(width = 0.8),
    hjust = -0.3,
    size = 7,
    fontface = "bold",
    show.legend = FALSE
  ) +
  theme_minimal(base_size = 20) +
  theme(
    legend.position = "top",
    legend.justification = "left",
    legend.direction = "horizontal",
    legend.box.spacing = unit(0.5, "cm"),
    legend.margin = margin(0, 0, 20, 0),
    legend.text = element_text(size = 20),
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title.x = element_text(size = 20, margin = margin(t = 15)),
    axis.text = element_text(size = 20, face = "bold"),
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    plot.margin = margin(20, 30, 20, 20)
  ) +
  theme_gdocs() +
  bbc_style()

finalise_plot(plot_name = grouped_bars, source = "Sourse: Data derived from IUCN, WWF, and environmental studies journals.", save_filepath = '/path/to/output/chart/chart_0047/chart.png', width_pixels = 896, height_pixels = 630)
"""
]
simple_column_chart = [
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Generation = c("Baby Boomers", "Generation X", "Millennials", "Generation Z"),
  AverageFamilySize = c(3.2, 2.9, 2.5, 2.3)
)

# Reorder generations chronologically
data$Generation <- factor(data$Generation, 
                         levels = c("Baby Boomers", "Generation X", "Millennials", "Generation Z"))

# Create custom color palette
custom_colors <- c("#3182bd", "#6baed6", "#9ecae1", "#c6dbef")

grouped_bars_20250306165454 <- ggplot(data, aes(x = Generation, y = AverageFamilySize, fill = Generation)) +
  geom_col(width = 0.7) +
  scale_fill_manual(values = custom_colors) +
  scale_y_continuous(limits = c(0, 3.5), breaks = seq(0, 3.5, 0.5)) +
  labs(title = "Family Size Trends by Generation",
       subtitle = "Family sizes have decreased across generations",
       x = "", 
       y = "Average Family Size",
       caption = "") +
  geom_text(aes(label = AverageFamilySize),
            position = position_stack(vjust = 0.5),
            color = "white", 
            fontface = "bold",
            size = 8) +
  theme_minimal(base_size = 20) +
  theme(
    legend.position = "bottom",
    legend.title = element_blank(),
    legend.text = element_text(size = 20),
    legend.spacing.x = unit(1, "cm"),
    plot.title = element_text(size = 24, face = "bold"),
    plot.subtitle = element_text(size = 20),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.text = element_text(size = 20, color = "black"),
    axis.text.x = element_text(angle = 0, hjust = 0.5),
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    plot.margin = margin(20, 20, 20, 20)
  ) + 
  theme_stata() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, 
              source = "Sourse: Data is sourced from national census data and research surveys by demographic institutions.", 
              save_filepath = '/path/to/output/chart/chart_0009/chart.png', 
              width_pixels = 896, 
              height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  AgeGroup = c("0-5", "6-12", "13-18", "19-25", "26+"),
  Percentage = c(12.5, 35.0, 25.0, 15.0, 12.5)
)

# Convert AgeGroup to factor with explicit order
data$AgeGroup <- factor(data$AgeGroup, levels = c("0-5", "6-12", "13-18", "19-25", "26+"))

grouped_bars_20250306165454 <- ggplot(data, aes(x = AgeGroup, y = Percentage, fill = AgeGroup)) +
  geom_col(width = 0.7, color = "white", alpha = 0.9) +
  geom_text_repel(
    aes(label = paste0(Percentage, "%")),
    size = 6.5,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    nudge_y = 3,
    direction = "y",
    segment.size = 0.6,
    segment.color = "gray60",
    min.segment.length = 0,
    show.legend = FALSE
  ) +
  scale_y_continuous(limits = c(0, 45), breaks = seq(0, 40, by = 10)) +
  scale_fill_nejm(alpha = 0.9) +
  labs(
    title = "Age Distribution in Same-Sex Parent Families",
    subtitle = "Children aged 6-12 comprise the majority in such families.",
    x = "",
    y = "Percentage (%)",
    caption = ""
  ) +
  theme_ipsum_rc(base_size = 20, axis_title_size = 22, plot_title_size = 28, subtitle_size = 22) +
  theme(
    legend.position = "none",
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    axis.text.x = element_text(size = 20, face = "bold"),
    axis.text.y = element_text(size = 20),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  theme_wsj() +
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data sourced from national statistics and demographic studies on family structures.", save_filepath = '/path/to/output/chart/chart_0027/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  AgeGroup = c("18-24", "25-34", "35-44", "45-54", "55-64", "65+"),
  PetOwnershipRate = c(60, 70, 65, 50, 45, 40)
)

# Create custom color palette
custom_colors <- pal_npg("nrc", alpha = 0.8)(6)

grouped_bars_20250306165454 <- ggplot(data, aes(x = AgeGroup, y = PetOwnershipRate, fill = AgeGroup)) +
  geom_col(width = 0.7) +
  geom_text_repel(
    aes(label = paste0(PetOwnershipRate, "%")),
    position = position_dodge(width = 0.7),
    size = 7,
    fontface = "bold",
    box.padding = 1.5,
    point.padding = 1,
    force = 10,
    direction = "y",
    vjust = -0.5,
    segment.size = 0.5,
    segment.color = "gray50",
    min.segment.length = 0,
    show.legend = FALSE
  ) +
  scale_fill_manual(values = custom_colors) +
  scale_y_continuous(limits = c(0, 100), breaks = seq(0, 100, 20), expand = expansion(mult = c(0, 0.15))) +
  labs(
    title = "Pet Ownership Rates Across Age Groups",
    subtitle = "Younger age groups demonstrate higher pet ownership than older age groups.",
    x = "",
    y = "Pet Ownership Rate (%)",
    caption = ""
  ) +
  theme_minimal(base_size = 20) +
  theme(
    legend.position = "none",
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank(),
    axis.title.y = element_text(margin = margin(r = 15), size = 22, face = "bold"),
    axis.text = element_text(size = 20, face = "bold"),
    axis.text.x = element_text(margin = margin(t = 10), color = "black"),
    axis.text.y = element_text(color = "black"),
    plot.title = element_text(size = 26, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 25)),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +
  theme_hc() +
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Source: Data is sourced from surveys by the Pet Food Manufacturers' Association and demographic research studies.", save_filepath = '/path/to/output/chart/chart_0038/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  AgeGroup = c("0-4", "5-9", "10-14", "15-19", "20+"),
  Count = c(150, 300, 350, 200, 100)
)

# Add custom color palette
age_colors <- c("#3498db", "#2ecc71", "#f1c40f", "#e74c3c", "#9b59b6")

grouped_bars_20250306165454 <- ggplot(data, aes(x = AgeGroup, y = Count, fill = AgeGroup)) +
  geom_col(width = 0.7, color = "white") +
  geom_text_repel(
    aes(label = Count),
    size = 8,
    fontface = "bold",
    box.padding = 1.2,
    point.padding = 1,
    force = 35,
    force_pull = 0.3,
    segment.size = 0.7,
    segment.color = "gray40",
    min.segment.length = 0.3,
    direction = "y",
    nudge_y = 20,
    show.legend = FALSE
  ) +
  scale_fill_manual(values = age_colors) +
  scale_y_continuous(limits = c(0, 420), expand = expansion(mult = c(0, 0.1))) +
  labs(
    title = "Age Distribution in Blended Families",
    subtitle = "Children aged 5-15 are most common in blended families",
    x = "Age Group",
    y = "Number of Children"
  ) +
  theme_ipsum_rc(base_size = 20, axis_title_size = 22) +
  theme(
    legend.position = "bottom",
    legend.title = element_blank(),
    legend.text = element_text(size = 20),
    legend.spacing.x = unit(0.5, "cm"),
    axis.text = element_text(size = 20, face = "bold"),
    axis.title = element_text(size = 22, face = "bold"),
    plot.title = element_text(size = 26, face = "bold"),
    plot.subtitle = element_text(size = 20),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank()
  ) + 
  theme_excel() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data sourced from national statistics agencies and family demographic studies.", save_filepath = '/path/to/output/chart/chart_0039/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Age.Group = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55+"),
  Mobility.Rate = c(9.5, 20.3, 18.7, 12.1, 8.2, 6.3)
)

# Create a custom color palette
custom_colors <- pal_npg("nrc", alpha = 0.8)(6)[c(1, 2, 3, 4, 5, 6)]

# Order data by mobility rate to improve visualization
data$Age.Group <- factor(data$Age.Group, 
                         levels = data$Age.Group[order(data$Mobility.Rate, decreasing = TRUE)])

grouped_bars_20250306165454 <- ggplot(data, aes(x = Age.Group, y = Mobility.Rate)) +
  geom_col(fill = custom_colors, width = 0.7, alpha = 0.9) +
  geom_text_repel(
    aes(label = paste0(Mobility.Rate, "%")),
    size = 7,               
    fontface = "bold",      
    box.padding = 0.8,        
    point.padding = 0.8,       
    force = 25,             
    force_pull = 0.4,       
    segment.size = 0.4,     
    segment.color = "gray40",
    min.segment.length = 0.3,
    direction = "y",
    nudge_y = 1.2,
    show.legend = FALSE    
  ) +
  labs(
    title = "Geographic Mobility Patterns by Age Group",
    subtitle = "Young adults show highest geographic mobility among age groups",
    y = "Mobility Rate (%)"
  ) +
  scale_y_continuous(
    limits = c(0, 25),
    breaks = seq(0, 25, 5),
    expand = expansion(mult = c(0, 0.15))
  ) +
  theme_stata() +
  theme(
    axis.text.x = element_text(size = 20, face = "bold", angle = 45, hjust = 1),
    axis.text.y = element_text(size = 20, face = "bold"),
    axis.title.x = element_blank(),
    axis.title.y = element_text(size = 22, face = "bold", margin = margin(r = 15)),
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    legend.position = "none",
    panel.grid.major.y = element_line(color = "gray90", linetype = "dashed"),
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Source: Data is sourced from census bureau studies and national statistical agencies.", save_filepath = '/path/to/output/chart/chart_0041/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Age.Group = c("20-29", "30-39", "40-49", "50-59"),
  Childcare.Cost.Percent = c(18.0, 22.5, 19.0, 15.0)
)

grouped_bars_20250306165454 <- ggplot(data, aes(x = Age.Group, y = Childcare.Cost.Percent, fill = Age.Group)) +
  geom_col(width = 0.7) +
  geom_text_repel(
    aes(label = paste0(Childcare.Cost.Percent, "%")),
    size = 6,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.8,
    force = 25,
    force_pull = 0.1,
    segment.size = 0.6,
    segment.color = "gray40",
    min.segment.length = 0.3,
    direction = "y",
    nudge_y = 2,
    show.legend = FALSE
  ) +
  scale_fill_nejm() +
  scale_y_continuous(limits = c(0, 30), breaks = seq(0, 30, 5)) +
  labs(
    title = "Childcare Financial Burden by Parent Age Group",
    subtitle = "The financial burden is highest for parents aged 30-39",
    x = "Age Group",
    y = "Percentage of Income (%)",
    fill = "Age Group"
  ) +
  theme_ipsum_rc(
    base_size = 20,
    base_family = "Helvetica",
    plot_title_size = 26,
    subtitle_size = 22,
    axis_title_size = 20
  ) +
  theme(
    legend.position = "bottom",
    legend.box.spacing = unit(1.5, "cm"),
    legend.key.size = unit(1.5, "cm"),
    legend.text = element_text(size = 20),
    legend.title = element_text(size = 22, face = "bold"),
    panel.grid.major.x = element_blank(),
    axis.text = element_text(size = 20, face = "bold"),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  theme_solarized() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data sourced from national childcare reports and income distribution studies", save_filepath = '/path/to/output/chart/chart_0045/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  Responses = c(1200, 1350, 1600, 1450, 1550),
  FinancialAidUSD = c(15.6, 16.2, 18.0, 17.5, 18.5)
)

grouped_bars_20250306165454 <- ggplot(data, aes(x = factor(Year), y = Responses, fill = as.factor(Year))) +
  geom_col(width = 0.7, color = "white", alpha = 0.9) +
  geom_text_repel(
    aes(label = Responses),
    size = 7,
    fontface = "bold",
    box.padding = 1.2,
    point.padding = 1.2,
    force = 30,
    force_pull = 0.5,
    segment.size = 0.7,
    segment.color = "gray50",
    min.segment.length = 0.2,
    direction = "y",
    nudge_y = 70,
    show.legend = FALSE
  ) +
  scale_fill_npg(name = "Year") +
  scale_y_continuous(limits = c(0, 1900), expand = c(0, 0)) +
  labs(
    title = "International Responses to Humanitarian Crises",
    subtitle = "Aid responses have fluctuated over the last five years (2018-2022)",
    x = "",
    y = "Number of Responses",
    caption = ""
  ) +
  theme_minimal(base_size = 20) +
  theme(
    plot.title = element_text(face = "bold", size = 24, margin = margin(b = 20)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.text = element_text(size = 20, face = "bold"),
    legend.position = "bottom",
    legend.title = element_text(size = 20),
    legend.text = element_text(size = 20),
    legend.spacing.x = unit(1, "cm"),
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    panel.grid.major.y = element_line(color = "gray90"),
    plot.margin = margin(20, 20, 20, 20)
  ) + 
  theme_excel() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Source: Data compiled from UNOCHA annual reports, International Red Cross statistics, and national aid agencies.", save_filepath = '/path/to/output/chart/chart_0049/chart.png', width_pixels = 896, height_pixels = 630)
"""
]
paired_column_chart = [
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  NAFTA = c(1100, 1150, 1200, 1250, 1280),
  EU = c(1300, 1350, 1400, 1450, 1520),
  ASEAN = c(700, 730, 750, 800, 820)
)

data_long <- reshape2::melt(data, id.vars = "Year", variable.name = "Bloc", value.name = "TradeVolume")

# Format the labels with "B" suffix for billions
data_long$label <- paste0(data_long$TradeVolume, "B")

# Create custom color palette
bloc_colors <- c("NAFTA" = "#0073C2", "EU" = "#EFC000", "ASEAN" = "#CD534C")

grouped_bars_20250306165454 <- ggplot(data_long, aes(x = factor(Year), y = TradeVolume, fill = Bloc)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.9), width = 0.8) +
  scale_fill_manual(values = bloc_colors) +
  labs(title = "Trends in Key Economic Blocs and Trade Partnerships",
       subtitle = "Trade volume comparison across NAFTA, EU, and ASEAN (2018-2022)",
       x = "", 
       y = "Trade Volume (in Billions USD)",
       caption = "") +
  geom_text(
    aes(label = label, y = TradeVolume + 30),
    position = position_dodge(width = 0.9),
    size = 6,
    fontface = "bold",
    show.legend = FALSE
  ) +
  scale_y_continuous(
    limits = c(0, 1700),
    breaks = seq(0, 1600, by = 400),
    expand = expansion(mult = c(0, 0.1))
  ) +
  theme_ipsum_rc(base_size = 20, base_family = "Helvetica") +
  theme(
    legend.position = "top",
    legend.title = element_blank(),
    legend.text = element_text(size = 22),
    legend.key.size = unit(1.5, "cm"),
    legend.spacing.x = unit(0.5, "cm"),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.text.x = element_text(size = 22, face = "bold"),
    axis.text.y = element_text(size = 22),
    plot.title = element_text(size = 26, face = "bold"),
    plot.subtitle = element_text(size = 22),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank()
  ) +
  theme_wsj() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data is sourced from WTO Annual Reports, World Bank trade reports, and international trade ministry publications.", save_filepath = '/path/to/output/chart/chart_0001/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Country = c("USA", "UK", "India", "Israel", "Nigeria", "Indonesia"),
  Military_Strategy_Effectiveness = c(75, 70, 68, 80, 65, 60),
  Non_Military_Strategy_Effectiveness = c(82, 85, 76, 72, 60, 70)
)

# Reorder countries for better presentation
data$Country <- factor(data$Country, levels = data$Country[order(data$Military_Strategy_Effectiveness, decreasing = TRUE)])

# Convert data to long format for easier manipulation
data_long <- reshape2::melt(data, id.vars = "Country", 
                            variable.name = "Strategy", 
                            value.name = "Effectiveness")

# Clean up strategy names for legend
data_long$Strategy <- gsub("_Strategy_Effectiveness", "", data_long$Strategy)

# Create improved plot
grouped_bars_20250306165454 <- ggplot(data_long, aes(x = Country, y = Effectiveness, fill = Strategy)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_fill_manual(values = c("Military" = "#E41A1C", "Non_Military" = "#4292C6")) +
  geom_text_repel(
    aes(label = Effectiveness, group = Strategy),
    position = position_dodge(width = 0.8),
    size = 7,
    fontface = "bold",
    box.padding = 0.5,
    point.padding = 0.5,
    force = 15,
    segment.color = "gray50",
    segment.size = 0.5,
    direction = "y",
    vjust = -0.5,
    show.legend = FALSE
  ) +
  labs(title = "Global Counterterrorism Strategies and Effectiveness",
       subtitle = "Comparing Military vs. Non-Military Approaches",
       x = "",
       y = "Effectiveness Score (0-100)",
       fill = "Strategy Type:") +
  scale_y_continuous(limits = c(0, 100), breaks = seq(0, 100, 20)) +
  theme_ipsum_ps(base_size = 20, base_family = "Arial") +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.margin = margin(t = 10, b = 20),
    legend.key.size = unit(1.5, "cm"),
    legend.title = element_text(size = 22, face = "bold"),
    legend.text = element_text(size = 22),
    plot.title = element_text(size = 26, face = "bold", margin = margin(b = 10)),
    plot.subtitle = element_text(size = 22, margin = margin(b = 25)),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.text.x = element_text(size = 22, face = "bold"),
    axis.text.y = element_text(size = 22),
    panel.grid.major.y = element_line(color = "gray90"),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank()
  ) +
  theme_fivethirtyeight() +
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data is sourced from UNODC and Global Terrorism Database reports.", save_filepath = '/path/to/output/chart/chart_0007/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  Latin_American = c(150, 170, 200, 220, 210),
  Asian = c(100, 105, 140, 130, 135),
  African = c(75, 80, 95, 90, 85)
)

data_long <- reshape2::melt(data, id.vars = "Year", variable.name = "Group", value.name = "Count")

# Define custom colors that are more distinguishable
custom_colors <- c("#FF5A5F", "#087E8B", "#F5B700") 

grouped_bars_20250306165454 <- ggplot(data_long, aes(x = factor(Year), y = Count, fill = Group)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.9), width = 0.8) +
  geom_text_repel(
    aes(label = Count),
    size = 6,
    fontface = "bold",
    point.padding = 0.5,
    segment.size = 0.5,
    segment.color = "gray50",
    direction = "y",
    show.legend = FALSE,
    position = position_dodge(width = 0.9),
    vjust = -0.5
  ) +
  scale_fill_manual(values = custom_colors) +
  scale_y_continuous(limits = c(0, 250), expand = expansion(mult = c(0, 0.15))) +
  labs(
    title = "Hate Crime Trends Against Immigrants (2018-2022)",
    subtitle = "Significant variations in hate crime rates among different immigrant communities",
    x = "",
    y = "Number of Incidents",
    fill = "Immigrant Group"
  ) +
  theme_minimal(base_size = 20) +
  theme(
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_line(color = "grey90"),
    text = element_text(face = "plain"),
    legend.position = "top",
    legend.title = element_text(face = "bold"),
    legend.text = element_text(size = 20),
    legend.spacing.x = unit(1, "cm"),
    plot.title = element_text(face = "bold", size = 24, margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title.y = element_text(margin = margin(r = 10)),
    axis.text = element_text(face = "bold")
  ) +
  theme_hc() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data sourced from government crime statistics reports and international human rights databases.", save_filepath = '/path/to/output/chart/chart_0021/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  AgeGroup = c("20-29", "30-39", "40-49", "50+"),
  `1-5 Years` = c(55, 30, 20, 10),
  `6-10 Years` = c(35, 45, 30, 20),
  `11-20 Years` = c(20, 25, 35, 30)
)

data_melted <- reshape2::melt(data, id.vars = "AgeGroup", variable.name = "MarriageDuration", value.name = "DivorceRate")

# Set custom colors for better visual appeal
custom_colors <- c("#FF5A5F", "#3C91E6", "#7B5EA5")

grouped_bars_20250306165454 <- ggplot(data_melted, aes(x = AgeGroup, y = DivorceRate, fill = MarriageDuration)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.85), width = 0.75, alpha = 0.9) +
  geom_text_repel(
    aes(label = paste0(DivorceRate, "%")),
    position = position_dodge(width = 0.85),
    size = 6,  # Increased text size
    fontface = "bold",
    box.padding = 0.3,
    point.padding = 0.5,
    force = 10,
    direction = "y",
    vjust = -0.5,
    segment.color = "gray60",
    segment.size = 0.4,
    min.segment.length = 0,
    max.overlaps = 20,
    show.legend = FALSE
  ) +
  scale_fill_manual(values = custom_colors) +
  scale_y_continuous(limits = c(0, 70), breaks = seq(0, 70, 10), expand = expansion(mult = c(0, 0.15))) +
  labs(
    title = "Divorce Rates by Age Group and Marriage Duration",
    subtitle = "Younger age groups show higher divorce rates within short marriage durations",
    x = "Age Group",
    y = "Divorce Rate (%)",
    fill = "Marriage Duration"
  ) +
  theme_ipsum_ps(base_size = 20, base_family = "Helvetica") +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box.spacing = unit(0.5, "cm"),
    legend.key.size = unit(1, "cm"),
    legend.spacing.x = unit(1, "cm"),
    legend.title = element_text(face = "bold", size = 22),
    legend.text = element_text(size = 20, margin = margin(r = 20)),
    axis.title.x = element_text(face = "bold", margin = margin(t = 15), size = 22),
    axis.title.y = element_text(face = "bold", margin = margin(r = 15), size = 22),
    axis.text = element_text(size = 20, face = "bold"),
    plot.title = element_text(size = 24, face = "bold", margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 25)),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank()
  ) + 
  theme_tufte() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, source = "Sourse: Data is sourced from National Statistical Office and Family Studies Institute reports.", save_filepath = '/path/to/output/chart/chart_0028/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Country = c("France", "Japan", "Brazil"),
  Pre_Reform_Avg_Pension_2015 = c(1500, 1300, 900),
  Post_Reform_Avg_Pension_2020 = c(1600, 1350, 950),
  Retirement_Age_2015 = c(62, 65, 60),
  Retirement_Age_2020 = c(64, 67, 62),
  Elderly_Population_Percent_2015 = c(19.0, 26.0, 8.5),
  Elderly_Population_Percent_2020 = c(21.0, 28.7, 10.2)
)

data_long <- reshape2::melt(
  data,
  id.vars = "Country",
  measure.vars = c("Pre_Reform_Avg_Pension_2015", "Post_Reform_Avg_Pension_2020"),
  variable.name = "Period",
  value.name = "Pension"
)

# Clean up period labels
data_long$Period <- factor(data_long$Period, 
                           levels = c("Pre_Reform_Avg_Pension_2015", "Post_Reform_Avg_Pension_2020"),
                           labels = c("2015 (Pre-Reform)", "2020 (Post-Reform)"))

# Create better positioning for labels
data_long$label_y <- data_long$Pension + 50

grouped_bars <- ggplot(data=data_long, aes(x=Country, y=Pension, fill=Period)) +
  geom_bar(stat="identity", position=position_dodge(width=0.8), width=0.7) +
  geom_text(
    aes(y = label_y, label = paste0("$", format(Pension, big.mark=","))),
    position = position_dodge(width=0.8),
    size = 7,
    fontface = "bold",
    vjust = 0.5,
    show.legend = FALSE
  ) +
  scale_fill_jama(alpha = 0.9) +
  scale_y_continuous(
    limits = c(0, 2000),
    breaks = seq(0, 2000, by = 500),
    expand = expansion(mult = c(0, 0.15)),
    labels = function(x) paste0("$", format(x, big.mark = ","))
  ) +
  labs(
    title = "Impact of Pension Reforms (2015-2020)",
    subtitle = "Average monthly pension payments before and after reforms",
    caption = "",
    x = "",
    y = "Average Monthly Pension",
    fill = "Time Period"
  ) +
  theme_ipsum_rc(grid="Y", base_size = 20) +
  theme(
    legend.position = "top",
    legend.direction = "horizontal",
    legend.title = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 20),
    legend.key.size = unit(1.5, "cm"),
    plot.title = element_text(size = 26, face = "bold", margin = margin(b = 10)),
    plot.subtitle = element_text(size = 22, margin = margin(b = 20)),
    axis.title.y = element_text(size = 22, margin = margin(r = 15)),
    axis.text = element_text(size = 20, face = "bold"),
    panel.grid.major.y = element_line(color = "gray90", size = 0.5),
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +
  theme_solarized() +
  bbc_style()

finalise_plot(plot_name = grouped_bars, source = "Sourse: World Bank, OECD, and national statistics offices", save_filepath = '/path/to/output/chart/chart_0030/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Voting_System = c("First-Past-The-Post", "Ranked Choice", "Proportional Representation"),
  Year = c(2022, 2022, 2022),
  Vote_Share_Percent = c(40, 38, 22),
  Success_Rate_Percent = c(45, 42, 33),
  Seats_Won = c(30, 28, 42)
)

# Convert Voting_System to factor with desired order
data$Voting_System <- factor(data$Voting_System, 
                             levels = c("First-Past-The-Post", "Ranked Choice", "Proportional Representation"))

# Reshape data for grouped bar chart
data_long <- reshape2::melt(data, id.vars = c("Voting_System", "Year"), 
                            measure.vars = c("Vote_Share_Percent", "Success_Rate_Percent"),
                            variable.name = "Metric", value.name = "Value")

# Make metric names more readable
data_long$Metric <- factor(data_long$Metric,
                          levels = c("Vote_Share_Percent", "Success_Rate_Percent"),
                          labels = c("Vote Share", "Success Rate"))

# Create the plot
grouped_bars_20250306165454 <- ggplot(data_long, aes(x = Voting_System, y = Value, fill = Metric)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7, alpha = 0.9) +
  geom_text_repel(
    aes(label = paste0(Value, "%"), group = Metric),
    position = position_dodge(width = 0.8),
    size = 7,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    force = 20,
    segment.size = 0.6,
    segment.color = "gray40",
    direction = "y",
    vjust = -0.5,
    show.legend = FALSE
  ) +
  labs(title = "Comparative Analysis of Voting Systems (2022)",
       subtitle = "Vote share and candidate success rates across different electoral systems",
       x = "",
       y = "Percentage (%)",
       caption = "") +
  scale_fill_manual(values = c("Vote Share" = "#3182bd", "Success Rate" = "#31a354"),
                   name = "") +
  scale_y_continuous(limits = c(0, 60), breaks = seq(0, 60, 10)) +
  theme_minimal(base_size = 20) +
  theme(
    plot.title = element_text(size = 24, face = "bold", hjust = 0.5),
    plot.subtitle = element_text(size = 20, hjust = 0.5, margin = margin(b = 20)),
    axis.title.y = element_text(size = 20, margin = margin(r = 10)),
    axis.text = element_text(size = 20),
    axis.text.x = element_text(size = 20, face = "bold"),
    legend.position = "top",
    legend.text = element_text(size = 20),
    legend.key.size = unit(1.5, "cm"),
    legend.spacing.x = unit(1, "cm"),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank(),
    panel.border = element_blank(),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +
  theme_wsj() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, 
              source = "Sourse: Derived from electoral studies and political science publications.", 
              save_filepath = '/path/to/output/chart/chart_0035/chart.png', 
              width_pixels = 896, 
              height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)
library(tidyr)
library(dplyr)

data <- data.frame(
  Age_Group = c("25-34", "35-44", "45-54"),
  Adventure = c(40, 30, 20),
  Relaxation = c(25, 40, 50),
  Cultural = c(35, 30, 30)
)

data_long <- data %>%
  pivot_longer(-Age_Group, names_to = "Type", values_to = "Percentage")

# Reordering factors for better presentation
data_long$Age_Group <- factor(data_long$Age_Group, levels = c("25-34", "35-44", "45-54"))
data_long$Type <- factor(data_long$Type, levels = c("Adventure", "Cultural", "Relaxation"))

grouped_bars_20250306165454 <- ggplot(data_long, aes(x = Age_Group, y = Percentage, fill = Type)) +
  geom_col(position = position_dodge(width = 0.9), width = 0.8, color = "white", alpha = 0.9) +
  geom_text_repel(
    aes(label = paste0(Percentage, "%")),
    position = position_dodge(width = 0.9),
    size = 7,
    fontface = "bold",
    box.padding = 0.8,
    point.padding = 0.5,
    segment.color = "gray50",
    segment.size = 0.7,
    min.segment.length = 0.1,
    direction = "y",
    force = 3,
    show.legend = FALSE
  ) +
  scale_fill_npg(name = "Vacation Type") +
  scale_y_continuous(limits = c(0, 60), breaks = seq(0, 60, 10), expand = expansion(mult = c(0, 0.1))) +
  labs(
    title = "Family Vacation Preferences by Parental Age Group",
    subtitle = "Preferences vary by age: younger parents favor adventure trips",
    x = "Age Group",
    y = "Percentage (%)"
  ) +
  theme_minimal(base_size = 20, base_family = "Avenir") +
  theme(
    legend.position = "top",
    legend.title = element_text(face = "bold", size = 22),
    legend.text = element_text(size = 20),
    legend.key.size = unit(1.5, "cm"),
    legend.spacing.x = unit(0.5, "cm"),
    plot.title = element_text(face = "bold", size = 24, margin = margin(b = 15)),
    plot.subtitle = element_text(size = 20, margin = margin(b = 20)),
    axis.title.x = element_text(size = 22, face = "bold", margin = margin(t = 15)),
    axis.title.y = element_text(size = 22, face = "bold", margin = margin(r = 15)),
    axis.text = element_text(size = 20, color = "black"),
    panel.grid.major.y = element_line(color = "gray90"),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank(),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +
  theme_excel() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars_20250306165454, 
              source = "Sourse: Survey data from Family Travel Studies and Travel Association Reports", 
              save_filepath = '/path/to/output/chart/chart_0045/chart.png', 
              width_pixels = 896, 
              height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
  Department = c("Sales", "Marketing", "Product Development", "Human Resources", "Finance"),
  Low_Stress = c(50, 53, 62, 57, 60),
  Medium_Stress = c(45, 48, 55, 50, 52),
  High_Stress = c(38, 40, 45, 43, 44)
)

data_long <- reshape2::melt(data, id.vars = "Department", variable.name = "Stress_Level", value.name = "Productivity")

# Reorder factor levels for better visual understanding
data_long$Stress_Level <- factor(data_long$Stress_Level, 
                                levels = c("Low_Stress", "Medium_Stress", "High_Stress"))

# Rename factor levels for better readability in legend
levels(data_long$Stress_Level) <- c("Low Stress", "Medium Stress", "High Stress")

grouped_bars <- ggplot(data_long, aes(x = Department, y = Productivity, fill = Stress_Level)) +
  geom_bar(stat = 'identity', position = position_dodge(width = 0.9), width = 0.8) +
  geom_text_repel(
    aes(label = Productivity, group = Stress_Level),
    position = position_dodge(width = 0.9),
    size = 5,
    fontface = "bold",
    box.padding = 0.5,
    point.padding = 0.5,
    force = 2,
    segment.size = 0.2,
    segment.color = "gray50",
    direction = "y",
    show.legend = FALSE
  ) +
  scale_fill_jama() +
  scale_y_continuous(limits = c(0, 70), breaks = seq(0, 70, 10)) +
  labs(
    title = "Work-Related Stress vs. Employee Productivity",
    subtitle = "Higher stress levels correlate with reduced productivity",
    x = "Department",
    y = "Productivity Score",
    fill = "Stress Level"
  ) +
  theme_ipsum_rc(base_size = 20) +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1, size = 20),
    axis.text.y = element_text(size = 20),
    axis.title = element_text(size = 22, face = "bold"),
    plot.title = element_text(size = 24, face = "bold"),
    plot.subtitle = element_text(size = 22),
    legend.title = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 20),
    legend.position = "top",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    legend.spacing.x = unit(1, "cm"),
    legend.key.size = unit(1, "cm")
  ) +
  theme_gdocs() + 
  bbc_style()

finalise_plot(plot_name = grouped_bars, source = "Sourse: Data is derived from internal HR reports and wellness assessments.", save_filepath = '/path/to/output/chart/chart_0046/chart.png', width_pixels = 896, height_pixels = 630)
""",
"""
library(ggplot2)
library(ggrepel)
library(hrbrthemes)
library(bbplot)
library(ggsci)
library(ggthemes)

data <- data.frame(
    Age_Group = c("18-24", "25-34", "35-44"),
    High_School = c(30, 50, 40),
    Bachelors_Degree = c(25, 55, 50),
    Graduate_Degree = c(20, 60, 65)
)

# Convert data to long format
data_long <- reshape2::melt(data, id.vars = "Age_Group")

# Rename the education levels for better display
data_long$variable <- factor(data_long$variable, 
                           levels = c("High_School", "Bachelors_Degree", "Graduate_Degree"),
                           labels = c("High School", "Bachelor's Degree", "Graduate Degree"))

# Create optimized plot
grouped_bars <- ggplot(data_long, aes(x = Age_Group, y = value, fill = variable)) +
    geom_col(position = position_dodge(width = 0.8), width = 0.7) +
    geom_text_repel(
        aes(label = value, group = variable),
        position = position_dodge(width = 0.8),
        size = 6,
        fontface = "bold",
        box.padding = 0.8,
        point.padding = 0.5,
        min.segment.length = 0,
        direction = "y",
        hjust = 0.5,
        vjust = -0.5,
        segment.color = "gray50",
        segment.size = 0.5,
        show.legend = FALSE
    ) +
    labs(title = "Family Planning Decisions by Age and Education",
         subtitle = "Age and education impact family planning decisions differently",
         x = "Age Group",
         y = "Number of Responses",
         fill = "Education Level") +
    scale_y_continuous(limits = c(0, 75), breaks = seq(0, 70, 10)) +
    scale_fill_npg() +
    theme_ipsum_rc(
        base_size = 20,
        base_family = "Helvetica",
        plot_title_size = 26,
        subtitle_size = 22,
        axis_title_size = 22,
        axis_text_size = 20
    ) +
    theme(
        legend.position = "bottom", 
        legend.box = "horizontal",
        legend.title = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 20),
        legend.key.size = unit(1.5, "cm"),
        legend.spacing.x = unit(0.5, "cm"),
        axis.title.y = element_text(margin = margin(r = 15)),
        axis.title.x = element_text(margin = margin(t = 15)),
        plot.title = element_text(face = "bold"),
        plot.margin = margin(20, 20, 20, 20)
    ) +
    theme_wsj() +
    bbc_style()

finalise_plot(plot_name = grouped_bars, source = "Sourse: Data derived from demographic and health surveys.", save_filepath = '/path/to/output/chart/chart_0048/chart.png', width_pixels = 896, height_pixels = 630)
"""
]

chart_themes = [
         "theme_economist()",
         "theme_fivethirtyeight()",
         "theme_wsj()",
         "theme_stata()",
         "theme_excel()",
         "theme_tufte()",
         "theme_solarized()",
         "theme_hc()",
         "theme_map()",
         "theme_gdocs()",
         "theme_pander()",
         "theme_few()",
         "theme_igray()",
         "theme_calc()",
         "theme_par()"
     ]

color_matchings = [
         "scale_color_tableau()",
         "scale_color_economist()",
         "scale_color_wsj()",
         "scale_color_fivethirtyeight()",
         "scale_color_stata()",
         "scale_color_excel()",
         "scale_color_colorblind()",
         "scale_color_ptol()",
         "scale_color_few()",
         "scale_color_hc()",
         "scale_color_solarized()",
         "scale_color_gdocs()",
         "scale_color_pander()",
         "scale_color_calc()",
         "scale_color_continuous_tableau()",
         "scale_color_highlight()",
         "scale_color_solarized_light()",
         "scale_color_canva()",
         "scale_color_gradient()",
         "scale_color_npg()",
         "scale_color_aaas()",
         "scale_color_nejm()",
         "scale_color_jco()",
         "scale_color_gsea()"
     ]


topics = [
    "Correlation between parental age and number of children",
    "Age gaps in marriages: trends over time",
    "Multi-generational households by geographic region",
    "Impact of delayed parenthood on family size",
    "Single-parent household age demographics",
    "Age distribution of adoptive parents",
    "Grandparents serving as primary caregivers: age analysis",
    "Life expectancy variations based on family structure",
    "Family size trends by generation",
    "Age of independence: when young adults leave home by country",
    "Elderly living arrangements: alone vs. with family",
    "Divorce rates by age group and marriage duration",
    "Age-related patterns in remarriage rates",
    "The financial burden of childcare across parent age groups",
    "Correlation between maternal age and birth outcomes",
    "Age distribution in blended families",
    "Work-life balance satisfaction by parent age",
    "Sibling age gaps: trends and implications",
    "Family reunion frequency by generational age groups",
    "Age patterns in custody arrangements after divorce",
    "Extended family involvement by cultural background and age",
    "Parenting style differences across age cohorts",
    "Digital technology use in families by age group",
    "Age-related trends in family meal frequency",
    "Family planning decisions by age and education level",
    "Paternity leave usage rates by father's age",
    "Age factors in international adoption patterns",
    "Loneliness indicators across family structures and ages",
    "Financial support patterns between adult children and aging parents",
    "Age demographics of childfree couples by choice",
    "Intergenerational wealth transfer timing and amounts",
    "Family vacation trends by parental age",
    "Changing perceptions of ideal family size by generation",
    "Impact of delayed retirement on extended family dynamics",
    "Pet ownership as substitute for children by age group",
    "Age of parents when children reach key milestones",
    "Sandwich generation: caring for children and parents simultaneously",
    "Family communication methods by age cohort",
    "Religious observance in families by generational age",
    "Health outcomes correlated with family structure and age",
    "Housing choices based on family composition and age",
    "Geographic mobility patterns in families by age",
    "Impact of student debt on family formation by age",
    "Age distribution in same-sex parent families",
    "Trends in immigration patterns over the past two decades",
    "Correlation between immigration rates and economic growth",
    "Demographic shifts due to immigration in major urban areas",
    "Effects of immigration policies on workforce diversity",
    "Statistical analysis of asylum seeker acceptance rates",
    "The impact of immigration on housing markets",
    "Trends in interracial marriages and their societal impact",
    "Educational attainment levels among immigrant populations",
    "Economic contributions of immigrant entrepreneurs",
    "Public perception of immigration based on media coverage",
    "Impact of immigration on crime rates: a data-driven approach",
    "Changes in racial demographics due to migration flows",
    "Generational differences in attitudes toward immigration",
    "Representation of racial minorities in government and leadership",
    "Correlation between immigration status and healthcare access",
    "Effect of immigration on public service usage",
    "Distribution of immigrant populations across rural and urban areas",
    "Historical trends in migration due to conflicts and wars",
    "Statistical analysis of deportation rates and their causes",
    "Impact of immigration on language diversity in host countries",
    "Differences in employment rates between native and immigrant populations",
    "Influence of immigration status on wage gaps",
    "Trends in racial and ethnic segregation in housing",
    "Correlation between immigration and innovation in technology sectors",
    "Changes in birth rates among immigrant families",
    "Disparities in healthcare outcomes among racial and immigrant groups",
    "Trends in second-generation immigrant educational performance",
    "The role of remittances in global economic shifts",
    "Statistical analysis of refugee resettlement success rates",
    "Gender differences in migration trends and labor participation",
    "Long-term effects of immigration on cultural integration",
    "Social mobility trends among immigrant communities",
    "The impact of Brexit on migration trends in the UK",
    "Data analysis of racial profiling in law enforcement",
    "Trends in citizenship acquisition among immigrants",
    "Comparative analysis of immigration policies across different countries",
    "Racial disparities in access to financial services",
    "Correlation between racial diversity and economic resilience",
    "Impact of family reunification policies on immigration patterns",
    "Trends in public support for immigration policies",
    "Effects of border enforcement measures on migration flows",
    "Analysis of hate crime trends against immigrant populations",
    "Social and economic integration of undocumented immigrants",
    "Differences in political engagement among racial and immigrant groups",
    "Data-driven insights on brain drain and skilled migration",
    "Correlation between immigration and urban infrastructure development",
    "Comparative study of refugee acceptance rates by region",
    "Trends in international student migration and their economic impact",
    "Racial representation in professional sports and entertainment industries",
    "Statistical modeling of migration responses to climate change",
    "Trends in voter turnout over the past two decades",
    "Impact of social media on political engagement",
    "Correlation between economic conditions and election outcomes",
    "Public trust in government institutions: a data analysis",
    "Trends in political polarization across different age groups",
    "Effectiveness of government policies in reducing income inequality",
    "Analysis of policy shifts following changes in political leadership",
    "Impact of lobbying on legislative decision-making",
    "Comparative study of voting systems and election outcomes",
    "Public opinion trends on taxation policies",
    "Effects of term limits on political stability",
    "Correlation between education levels and political preferences",
    "Trends in public trust in the judiciary",
    "Statistical analysis of government spending efficiency",
    "Patterns in foreign aid distribution and geopolitical influence",
    "Changes in party affiliation across demographic groups",
    "Analysis of media bias in political reporting",
    "Trends in public opinion on climate change policies",
    "Impact of populism on democratic institutions",
    "Effects of minimum wage policies on employment rates",
    "Public response to government handling of crises",
    "Comparative analysis of healthcare policies across nations",
    "Influence of campaign financing on election outcomes",
    "Trends in policy responses to immigration issues",
    "Correlation between crime rates and law enforcement policies",
    "Effects of political scandals on party approval ratings",
    "Analysis of defense spending trends and global security",
    "Impact of fiscal policies on economic growth",
    "Trends in government surveillance and privacy concerns",
    "Patterns in diplomatic relations and trade agreements",
    "Effect of gerrymandering on election outcomes",
    "Analysis of pension reforms and aging populations",
    "Trends in public approval ratings of world leaders",
    "Data-driven insights on protests and civil unrest",
    "The role of think tanks in shaping public policy",
    "Trends in gender representation in political leadership",
    "Impact of automation on government labor policies",
    "Analysis of voting behavior among first-time voters",
    "Public opinion shifts on wealth redistribution policies",
    "Effects of environmental regulations on economic performance",
    "Comparative study of press freedom and political stability",
    "Statistical analysis of corruption perceptions worldwide",
    "Impact of regional policies on rural-urban migration",
    "Trends in government debt and fiscal responsibility",
    "Correlation between media consumption and political beliefs",
    "Analysis of foreign policy decisions and public approval",
    "Patterns in trade policy shifts following major elections",
    "Public response to government handling of pandemics",
    "The role of central banks in economic policy-making",
    "Trends in digital governance and e-voting adoption",
     "Trends in global religious affiliation over the past century",
    "Correlation between religiosity and levels of education",
    "Impact of migration on religious diversity in urban areas",
    "Patterns in religious conversion and secularization",
    "Influence of religious beliefs on voting behavior",
    "Trends in interfaith marriages and their societal impact",
    "Analysis of religious attendance across different age groups",
    "Impact of cultural globalization on traditional religious practices",
    "Patterns in religious conflict and resolution efforts",
    "Correlation between religious identity and charitable giving",
    "Trends in religious representation in government leadership",
    "Impact of digital media on religious engagement",
    "Shifts in public attitudes towards religious institutions",
    "Comparative analysis of religious festivals and economic impact",
    "Patterns in media portrayals of different religious groups",
    "Influence of religious beliefs on attitudes toward gender roles",
    "Trends in the secularization of public policies",
    "Demographic trends in monastic and clergy populations",
    "Analysis of pilgrimage tourism and its economic significance",
    "Cultural impact of religious symbolism in fashion and art",
    "Patterns in youth participation in religious organizations",
    "Effects of religious beliefs on end-of-life care decisions",
    "Public attitudes toward religious education in schools",
    "Trends in the preservation and decline of indigenous religions",
    "Influence of religious doctrines on environmental activism",
    "Data analysis of hate crimes targeting religious communities",
    "Shifts in religious perspectives on LGBTQ+ rights",
    "Impact of religious affiliation on mental health trends",
    "Comparative study of fasting practices across religions",
    "Analysis of the role of religious leaders in social movements",
    "Patterns in religious influence on family structures",
    "Trends in global missionary work and religious outreach",
    "The role of religion in shaping cultural identity",
    "Correlation between religious affiliation and economic mobility",
    "Trends in religious-based dietary practices and consumption",
    "Impact of religious extremism on global security policies",
    "Patterns in religious influence on legal systems worldwide",
    "Public perception of religious freedom and government policies",
    "Analysis of religious influence on traditional medicine practices",
    "Trends in religious-themed literature and media consumption",
    "Demographic analysis of faith-based communities in rural areas",
    "Influence of religious beliefs on perspectives toward artificial intelligence",
    "Patterns in religious naming conventions and cultural heritage",
    "Comparative study of funeral and burial practices across cultures",
    "Trends in religious participation in humanitarian aid efforts",
    "Impact of economic crises on religious adherence",
    "Statistical analysis of religious conflict resolution initiatives",
    "Correlation between religious affiliation and happiness indices",
    "Trends in religious censorship and artistic expression",
    "Impact of religious doctrines on population growth patterns",
    "Trends in global income inequality over the past century",
    "Impact of automation on job market dynamics",
    "Correlation between education levels and wage growth",
    "Trends in remote work adoption across industries",
    "Impact of minimum wage policies on employment rates",
    "Comparative analysis of gender pay gaps across countries",
    "Trends in labor force participation among different age groups",
    "Effects of inflation on household purchasing power",
    "Statistical analysis of gig economy growth trends",
    "Impact of economic recessions on unemployment rates",
    "Trends in government stimulus policies and economic recovery",
    "Public perceptions of job security in different industries",
    "The role of trade unions in modern labor markets",
    "Correlation between work-life balance and job satisfaction",
    "Trends in corporate tax policies and business growth",
    "Impact of economic globalization on local job markets",
    "Statistical analysis of foreign direct investment trends",
    "Patterns in entrepreneurship and small business success rates",
    "Effects of workplace diversity on company performance",
    "Trends in retirement age and pension sustainability",
    "Impact of climate policies on employment in energy sectors",
    "Correlation between economic downturns and mental health trends",
    "Trends in youth unemployment and job training programs",
    "Effects of labor migration on domestic job markets",
    "Impact of consumer spending habits on economic growth",
    "Statistical analysis of wealth accumulation across generations",
    "Trends in corporate layoffs and restructuring strategies",
    "The role of financial literacy in economic mobility",
    "Patterns in work-related stress and employee productivity",
    "Impact of flexible work arrangements on business efficiency",
    "Effects of government debt on national economic stability",
    "Trends in the adoption of universal basic income policies",
    "Statistical analysis of workplace automation and job displacement",
    "Comparative study of economic growth in developed vs. developing nations",
    "Impact of stock market fluctuations on retirement savings",
    "Trends in international trade agreements and economic impact",
    "Effects of digital currencies on global financial markets",
    "Correlation between urbanization and local economic growth",
    "Trends in CEO compensation and corporate performance",
    "Analysis of wage stagnation and economic productivity",
    "The role of artificial intelligence in transforming labor markets",
    "Trends in corporate social responsibility and consumer trust",
    "Impact of pandemic-related policies on global employment rates",
    "Comparative study of economic resilience in different regions",
    "Trends in work-related migration and economic development",
    "Statistical analysis of income taxation and wealth redistribution",
    "Effects of economic uncertainty on startup investments",
    "Patterns in job market recovery after financial crises",
    "Impact of digital transformation on employment opportunities",
    "Trends in job satisfaction and employee retention strategies",
    "Correlation between economic policies and business innovation",
    "Trends in global conflict and peace agreements over the past century",
    "Impact of economic sanctions on international trade",
    "Statistical analysis of refugee movements and resettlement patterns",
    "Trends in diplomatic relations between major world powers",
    "Effects of military alliances on regional stability",
    "Correlation between foreign aid and economic development",
    "Patterns in global defense spending and military capabilities",
    "Impact of international organizations on conflict resolution",
    "Trends in international arms trade and its economic impact",
    "Comparative analysis of soft power influence among global superpowers",
    "Impact of climate change policies on international relations",
    "Statistical trends in cross-border migration and its geopolitical impact",
    "Effects of economic globalization on national sovereignty",
    "Analysis of trade disputes and their effects on global markets",
    "Trends in cyber warfare and digital security policies",
    "Impact of global energy markets on international diplomacy",
    "Patterns in international treaties on environmental protection",
    "Comparative study of human rights policies across nations",
    "Trends in global governance and multilateral cooperation",
    "Effects of pandemics on international relations and travel policies",
    "Correlation between political stability and foreign direct investment",
    "Trends in international media influence on foreign policy decisions",
    "Impact of global food security issues on diplomatic relations",
    "Analysis of voting patterns in the United Nations",
    "Trends in border disputes and geopolitical tensions",
    "Comparative study of foreign policy shifts across different administrations",
    "Impact of regional conflicts on global security frameworks",
    "Statistical analysis of foreign election interference cases",
    "Trends in international economic blocs and trade partnerships",
    "Effects of space exploration policies on global cooperation",
    "Analysis of cultural diplomacy and its impact on international relations",
    "Trends in international responses to humanitarian crises",
    "Statistical insights into nuclear non-proliferation agreements",
    "Patterns in global counterterrorism strategies and effectiveness",
    "Impact of digital currencies on international financial systems",
    "Trends in diplomatic engagements between developing nations",
    "Comparative analysis of intelligence-sharing agreements worldwide",
    "Effects of shifting global supply chains on trade relations",
    "Correlation between press freedom and diplomatic tensions",
    "Statistical trends in foreign military interventions",
    "Impact of international environmental agreements on national policies",
    "Analysis of emerging economies and their influence on global politics",
    "Trends in international student migration and educational exchange programs",
    "Patterns in global leadership approval ratings",
    "Impact of water scarcity on transboundary conflicts",
    "Trends in foreign policy approaches to authoritarian regimes",
    "Effects of international labor migration on global workforce dynamics",
    "Statistical analysis of global public opinion on world leaders",
    "Trends in economic diplomacy and investment treaties",
    "Impact of artificial intelligence regulations on international cooperation",
    "Trends in global internet penetration over the past two decades",
    "Impact of social media algorithms on political polarization",
    "Statistical analysis of online misinformation and fact-checking",
    "Patterns in digital media consumption across different age groups",
    "Effects of internet censorship on freedom of speech",
    "Trends in online news readership and traditional media decline",
    "Impact of streaming services on global entertainment industries",
    "Comparative analysis of digital advertising effectiveness",
    "Trends in online privacy concerns and data protection policies",
    "Correlation between social media usage and mental health trends",
    "Statistical insights into cybercrime and online fraud incidents",
    "Effects of influencer marketing on consumer behavior",
    "Trends in global podcast consumption and audience demographics",
    "Impact of artificial intelligence on news content generation",
    "Patterns in media coverage of international conflicts",
    "Analysis of government regulation on internet platforms",
    "Trends in digital journalism and independent news platforms",
    "Effects of viral content on public perception of global events",
    "Comparative study of internet shutdowns and political stability",
    "Patterns in global social media engagement rates",
    "Impact of the gig economy on digital content creators",
    "Statistical analysis of digital piracy and copyright enforcement",
    "Trends in mobile internet usage and app-based economies",
    "Correlation between online political engagement and voter turnout",
    "Effects of misinformation campaigns on public health policies",
    "Patterns in internet access disparity across rural and urban areas",
    "Impact of blockchain technology on digital media distribution",
    "Trends in deepfake content and its implications on media trust",
    "Statistical analysis of digital literacy levels worldwide",
    "Patterns in online gaming communities and social interaction",
    "Impact of paywall models on journalism sustainability",
    "Trends in internet governance and global cybersecurity policies",
    "Effects of real-time news reporting on public opinion formation",
    "Analysis of user engagement on short-form video platforms",
    "Trends in AI-generated content and its ethical implications",
    "Statistical insights into online harassment and digital safety",
    "Correlation between online reviews and consumer purchasing behavior",
    "Trends in citizen journalism and its role in breaking news",
    "Patterns in media representation of different social groups",
    "Impact of subscription-based media platforms on content diversity",
    "Effects of government surveillance on digital communication trends",
    "Trends in smart device adoption and internet connectivity",
    "Analysis of internet outages and their economic consequences",
    "Comparative study of search engine biases in news recommendations",
    "Patterns in meme culture and its impact on online discourse",
    "Effects of online petitions and activism on policy changes",
    "Trends in esports growth and its influence on mainstream media",
    "Analysis of personalized news feeds and their effects on audience diversity",
    "Statistical insights into online learning platforms and educational access",
    "Impact of 5G technology on global digital media consumption",
     "Trends in global research funding across scientific disciplines",
    "Impact of artificial intelligence on accelerating scientific discoveries",
    "Statistical analysis of open-access publishing in scientific research",
    "Patterns in international collaboration on scientific projects",
    "Effects of climate change research on global policy decisions",
    "Trends in space exploration and private sector involvement",
    "Impact of genome editing technologies on medical advancements",
    "Correlation between government funding and scientific innovation",
    "Patterns in research ethics violations and academic misconduct",
    "Trends in renewable energy research and adoption rates",
    "Impact of big data analytics on scientific research efficiency",
    "Statistical analysis of gender representation in STEM fields",
    "Trends in nanotechnology research and real-world applications",
    "Effects of interdisciplinary research on scientific breakthroughs",
    "Patterns in global antibiotic resistance research and policy responses",
    "Trends in artificial intelligence applications in healthcare research",
    "Impact of neuroscience research on mental health treatments",
    "Statistical insights into global patent trends in scientific fields",
    "Effects of long-term space travel on human physiology",
    "Patterns in biodiversity research and conservation efforts",
    "Trends in human longevity research and life extension technologies",
    "Impact of machine learning on drug discovery processes",
    "Statistical analysis of global research productivity by country",
    "Trends in materials science research and emerging technologies",
    "Patterns in research funding disparities across institutions",
    "Impact of citizen science on public engagement in research",
    "Statistical trends in artificial intelligence ethics research",
    "Effects of quantum computing advancements on scientific simulations",
    "Trends in robotics research and automation in various industries",
    "Impact of social sciences research on public policy development",
    "Patterns in the replication crisis in psychological research",
    "Trends in human brain mapping and neuroimaging technologies",
    "Impact of climate modeling research on disaster preparedness",
    "Statistical analysis of the rise of preprint servers in scientific publishing",
    "Effects of personalized medicine research on healthcare outcomes",
    "Patterns in agricultural research and global food security",
    "Trends in space weather research and its impact on technology",
    "Impact of synthetic biology research on biotechnology industries",
    "Statistical insights into the commercialization of scientific research",
    "Trends in water scarcity research and sustainable solutions",
    "Effects of interdisciplinary collaborations on research output quality",
    "Patterns in research funding allocation between public and private sectors",
    "Trends in research on extraterrestrial life and astrobiology",
    "Impact of wearable technology research on health monitoring",
    "Statistical analysis of emerging research topics in physics",
    "Effects of AI-driven scientific paper generation on academic publishing",
    "Trends in brain-computer interface research and applications",
    "Impact of 3D printing research on healthcare and manufacturing",
    "Patterns in global infectious disease research funding",
    "Trends in ethical considerations in genetic engineering research"
]
