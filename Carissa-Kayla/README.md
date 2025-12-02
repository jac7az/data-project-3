## Carissa Chen and Kayla Kim

## Data Source

**Authenticated GitHub API**
- https://api.github.com/repos/{package name}/{package name}/commits
- packages: scikit-learn, pandas, matplotlib, plotly, numpy


## Challenges / Obstacles

<!-- - visualization challenges: difficulty generalizing reusable code for graphs using matplotlib for all packages
- query specifications: syntax specifications not in prior knowledge of developers, learned through external sources on internet 
- Used duckdb to help with saving the data into a database to query more easily -->

For visualization challenges, we had difficulty generalizing reusable code for graphs using matplotlib for all packages. For query specifications, the syntax specifications were not in prior knowledge of developers. With these challenges, we learned through external sources on internet and tried to use familiar tactics, like duckdb to help with saving the data into a database to query more easily.


## Analysis

Being the 5 major Python data-science packages, commit trends over the past three and six months show distinct differences in development momentum. Pandas demonstrates the strongest recent period of growth with an 88% increase in commits over the past three months and a 54% increase over the past six months. This suggests an active development and maintenance of the package. Numpy also displays a rapid growth of 78% over the past three months, but a decline of -18% over the past six months, implying that the growth is very new and release event motivated rather than long-term. Scikit-learn also demonstrates the steady growth trend with 52% growth over the past three months and 28% growth over the past six months, which is typical for normal maintenance and development post-prototype. On the other hand, Matplotlib shows great decline with -57% growth in the past three months and -39% growth in the past six months. This is consistent with the fact that the package is maturing and in no immediate need for updates or new features; it's stabilizing. Plotly has the most lack of growth with -100% growth in the past three months, which indicates either private or slowing development in the repository. Commit counts alone do not indicate development health. Our analysis also considers contributor factors and timing patterns to distinguish active maintenance from older packages. However,  matplotlib had the overall most commits with over 50,000 while the next highest was numpy at about 40000, but in terms of number of unique commiters, matplotlib had the 2nd lowest number of committers, only higher than the very-limited-number of commits plotly package. Pandas had the most with over 4000 users commit changes. This is inline with how pandas demonstrated the strongest period of recently while matplotlib had a big decline.


## Plot / Visualization

### total commits per package
![hourly commits](./visualizations/commit_counts_per_package.png)
![commiters per package](./visualizations/unique_commiters_per_package.png)

### time charts
![hourly commits](./visualizations/hourly_commits.png)
![daily commits](./visualizations/daily_commits.png)
![weekly commits](./visualizations/weekly_commits.png)
![monthly commits](./visualizations/monthly_commits.png)

### percent changes in packages

#### three month periods
![monthly commits](./visualizations/threemo_perc_change.png)
#### six month periods
![monthly commits](./visualizations/sixmo_perc_change.png)



## GitHub Repository to Code
https://github.com/jac7az/CaKa-dp3-Code
