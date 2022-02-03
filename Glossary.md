![](https://www.sfu.ca/big-data/sites/default/files/SFU_BigData_logo_horz_RGB.png =200x)

**[Table of Contents](#table-of-contents)**

**[Term Categories](#categories)**

# Glossary

### ADVANCED RESEARCH COMPUTING

Advanced research computing (ARC) provides massive computational horsepower and [storage](#storage-and-physical-data-sources) in a [cloud environment](#cloud-computing) to handle problems and data that are too complex for a single desktop computer. [^1],[^2] [#disciplines](#disciplines)

### ALGORITHM

A sequence of instructions telling a computer how to answer a specific question. [^3],[^4] [#processing](#processing)

### ANALYTICS

The process of using [statistical models](#machine-learning) and software to [transform data](#data-transformation) into useful [information](#information) and to draw conclusions towards effective decision making.[^3],[^4] [#disciplines](#disciplines)

### ARTIFICIAL INTELLIGENCE

A branch of computer science that allows machines to acquire and apply knowledge to handle new inputs and analyze patterns to solve diverse problems. [^39] [#disciplines](#disciplines)

### BEHAVIOUR(AL) ANALYTICS

A type of business [analytics](#analytics) that examines behavioural data about people to understand how and why individuals act the way they do and to make more accurate predictions for future behaviour.[^5],[^6] [#data-analysis](#data-analysis)

### BIG DATA

Refers to the massive amounts of [data](#data) generated around the world that is too large, complex or varied for traditional processing software. Its potential to be analyzed for valuable information is enabled by technology such as [advanced research computing](#advanced-research-computing). [^7],[^8] [#disciplines](#disciplines)

### CAUSAL INFERENCE

Determines whether observations made in one variable are the reason for an effect observed in another variable, possibly occurring at a later time. See also [correlation mining](#correlation-mining) and [predictive analytics](#predictive-analytics). [#data-analysis](#data-analysis)

### CLASSIFICATION

An approach in [machine learning](#machine-learning) where a program is [trained](#model-fitting) with labeled [data](#data) to determine which category a new  observation belongs to. See also [clustering](#clustering). [#data-analysis](#data-analysis)

### CLOUD COMPUTING

Access to data, [storage](#distributed-file-system), applications, and other computing resources made available to many users on-demand over the [Internet](#network) to improve [scalable computing power](#advanced-research-computing) and reliability. [^9],[^10] [#disciplines](#disciplines)

### CLUSTER

A [network](#network) of computers (or compute nodes) that work on tasks together in parallel. The concept is different from [clustering](#clustering).

### CLUSTERING

A [machine learning](#machine-learning) technique that groups similar data points together to uncover hidden structure. Unlike [classification](#classification), clustering does not require labelled training data and is a type of unsupervised learning. [#data-analysis](#data-analysis)

### COMPUTING WITH DATA

Learning from data using computing tools and programming languages, such as Python or R with large ecosystems of libraries providing a convenient level of abstraction and statistical methods that can be organized into data processing pipelines.[^28] [#disciplines](#disciplines)

### CORRELATION MINING

As a measure of association between two variables, correlation can be used for [prediction](#predictive-analytics) and indicate the presence of [causal relationship](#causal-inference). It does, however, not sufficiently imply causation. [^37] [#data-analysis](#data-analysis)

### CYBERSECURITY

A model in information security designed to govern and evaluate how an organization handles data when it is stored, transmitted or processed. This model emphasizes that data should not be accessed without authorization, should not be altered or compromised without authorization, and should be accessible upon legitimate request. See [Secure Computing](#secure-computing). [^40] [#disciplines](#disciplines)

### DATA

Collection of examples, observations, measurements, facts, points, or other items of information that can be represented in [structured](#structured-data) or [unstructured](#unstructured-data) form.

### DATABASE

An organized collection of [data](#data) that allows easy access, management, updating and analysis of data. Commonly used databases are MySQL, PostgreSQL, as well as various [NoSQL](#no-sql-database) options.[^3] [#storage](#storage)

### DATA AGGREGATION

- TODO

### DATA CLEANING

Careful removal of erroneous or unreliable data points. [#processing](#processing)

### DATA EXPLORATION AND PREPARATION

Exploratory data analysis (EDA) is a formative step in the [creation of models](#model-fitting). [Views of the data](#visualization) are used to learn about patterns or relationships among variables. This includes [data cleaning](#data-cleaning) and manipulation for further analysis. [#processing](#processing)

### DATA INTEGRATION

The process of combining information from different data sources in preparation for data processing. [^4] [#processing](#processing)

### DATA MINING

An analytical process where large datasets are explored or "mined" in search of meaningful patterns, relationships or insights. The process can include statistics, [machine learning](#machine-learning) or other forms of artificial intelligence.[^3],[^4] [#disciplines](#disciplines)

### DATA REPRESENTATION

The form in which [data](#data) are stored, processed and transmitted such that its [information content](#information) and [context](#metadata) are retained as much as possible. Choices of form are influenced by hardware, software or other constraints around processing and analysis resources. [^28] [#processing](#processing)

### DATA TRANSFORMATION

The process of converting data from [one form into another](#data-representation) to gain better [insight](#insight). For instance, converting [unstructured data](#unstructured-data) into [structured form](#structured-data) that can be analyzed further. [#processing](#processing)

### DATA SCIENCE

A multidisciplinary activity combining programming skills, math and statistical analysis, and sector-specific expertise to extract [insights](#insight) from [data](#data). Often performed in stages: 1. [Data Exploration and Preparation](#data-exploration-and-preparation), 2. [Data Representation](#data-representation) and [Transformation](#data-transformation), 3. [Computing with Data](#computing-with-data), 4. [Machine Learning](#machine-learning), 5. [Data Visualization and Presentation](#visualization). [^28],[^29] [#disciplines](#disciplines)

### DESCRIPTIVE ANALYTICS

An initial stage of data processing that involves creating a summary of historical data with the goal of answering the question, "What happened?"[^13],[^14] [#data-analysis](#data-analysis)

### DISTRIBUTED FILE SYSTEM

A mechanism that stores files on servers and allows clients, with permission, to store and process files as if they were stored on their own computer.[^15],[^16] [#storage](#storage)

### FEATURE

A key property that characterizes a data point (representing some real-world object) in the context of a [machine learning](#machine-learning) problem or other type of [analysis](#analytics).

### FEATURE ENGINEERING

A human-driven process of finding the most important [features](#feature) to develop [predictive](#predictive-analytics) models. Formerly, as "art" to the "science" of [machine learning](#machine-learning), [big data](#big-data) increasingly moves towards automated representation learning.

### FLEXIBLE SCHEMA

Unlike [SQL](#sql) databases with a [tabular](#tabular-data) [structure](#structured-data), objects or documents stored in a flexible schema can be different from one another.[^32] [#data-types](#data-types)

### GENERATIVE MODELING

[Fitting](#model-fitting) a [model](#machine-learning) that can generate synthetic data beyond [given observations](#data). 
For example, a language model trained on a collection of text can be used to suggest possible words to modify or continue a given phrase. [^28]

### GOODNESS OF FIT

Summarizes how well the values observed in the data agree with those values expected by the model. [#processing](#processing)

### INFORMATION

Meaning encoded in [data](#data) that answers questions to better understand a concept by interpreting data within the context of its problem setting or domain. See also data analysis [algorithms](#algorithm) and information [visualization](#visualization).  [^38]

### INSIGHT

Actionable [information](#information) gained by interpreting [data analysis](#analytics) results, helping people to make more informed decisions. [^38]

### IOT (INTERNET OF THINGS)

A system of [connected](#network), "smart" objects, including smartphones, wearables and smart-appliances, that collect and exchange information without requiring human interaction. The IoT is a huge generator of data.[^17],[^18] [#storage](#storage)

### KNOWLEDGE DISCOVERY

Aims to extract [insight](#insight) from data in [databases](#database). It involves a [number of steps](#data-science) including the evaluation and possibly [interpretation](#visualization) of [patterns](#data-mining) to gather [insight](#insight) and knowledge.[^35] [#disciplines](#disciplines)

### MACHINE LEARNING

A part of [artificial intelligence](#artificial-intelligence) that enables machines to learn from experience to perform certain tasks by using [algorithmic](#algorithm) models that are [trained](#model-fitting) to imitate patterns present in [data](#data) to support [prediction](#predictive-analytics), [data generation](#generative-modeling) and other forms of [data analytics](#analytics). [#disciplines](#disciplines)

### METADATA

Also called "data about data," it provides a [structured description](#structured-data) and context for a data point - document, image, or file - to help organize, find and understand the data. [^33] [#data-types](#data-types)

### MODEL FITTING

Optimizes [how well](#goodness-of-fit) a [machine learning model](#machine-learning) can make predictions for previously unseen test data. 

### NETWORK

A system where multiple computing devices are connected to each other to exchange information and resources through a data link. For example, the Internet.[^19],[^20]

### NETWORK ANALYSIS

Mapping and measuring the relationships between people, groups, organizations, computers and other connected entities. It is used to simplify complex relationships, to make them easier to analyze. [^21]

### NO-SQL DATABASE

A type of database designed to handle [large](#advanced-research-computing) volumes of data that [may not have a structure](#flexible-schema).  [#storage](#storage)

### PREDICTIVE ANALYTICS

A process for analyzing current [data](#data) to determine future events or other unknowns. Related to [descriptive](#descriptive-analytics) and [prescriptive analytics](#prescriptive-analytics), it draws on techniques from [data mining](#data-mining), modeling, [machine learning](#machine-learning) and statistics.[^3],[^28]

### PRESCRIPTIVE ANALYTICS

A type of [analytics](#analytics) with the goal of using data to determine the best course of action for a specific scenario. [^3] [#data-analysis](#data-analysis)

### REGRESSION

A type of [statistical model](#machine-learning) that [predicts](#predictive-analytics) numerical values (instead of [class labels](#classification)). [#data-analysis](#data-analysis)

### RELATIONSHIP MINING

Relationship mining examines associations between two or more variables in a dataset, for example, by [correlation mining](#correlation-mining) and [causal mining](#causal-inference). [#data-analysis](#data-analysis)

### SECURE COMPUTING

Efforts to ensure privacy and to protect data, devices and computing systems from harm such as hacking, damage, and malpractice, and mitigate service disruptions. [^22],[^4] [#disciplines](#disciplines)

### SQL

SQL is a language that works with structured, [tabular data](#tabular-data) allowing to query and construct such data. It forms a standard for many [database](#database) systems. [28] [#processing](#processing)

### STRUCTURED DATA

[Data](#data) that is organized into clearly defined fields associated with variables or attributes, such as dates, words, or numbers that are recorded for each observation or item. Items are often represented as rows of  [tabular spreadsheets](#tabular-data) that can be stored in a [database](#database) for easy processing and analysis.[^24],[^25] [#data-types](#data-types)

### TABULAR DATA

Data items or observations that are organized as rows that contain values under columns that correspond to specific variables or properties. [^30],[^31] [#data-types](#data-types)

### TEXT MINING

A process of analyzing [text](#unstructured-data) to capture key concepts, themes, relationships and trends.[^36] [#data-analysis](#data-analysis)

### UNSTRUCTURED DATA

Data that is not organized in a pre-defined way under a single data model. Examples include text, images, audio, or video. [^26],[^27] [#data-types](#data-types), [#lesson-01](#lesson-01)

### VISUALIZATION

Visual representation of data including plots, charts, maps and infographics to support people with tasks such as sensemaking, effective communication of information, and improved pattern detection. For example, flight operation using a radar screen that displays sensor data in real-time. [^11],[^12]  [#data-analysis](#data-analysis)

### VISUALIZATION DASHBOARD

Multiple interactive graphical views of [data](#data) that would be too complex if presented in a [single visualization](#visualization), for instance, to support complex narratives and [insights](#insight) by showing key performance indicators (KPIs) for monitoring of a business or other processes. [#data-analysis](#data-analysis)

# Categories

The categories offer an alternative grouping that helps to find related terms.

## Data Inquiry Disciplines <a id="disciplines"/>

## Data Analysis Techniques <a id="data-analysis"/>

## Data Processing <a id="processing"/>

## Storage and Physical Data Sources <a id="storage"/>

## Types of Data <a id="data-types"/>

# Lessons

## Lessons 01 and 02 <a id="lesson-01"/>

## Lesson 03 <a id="lesson-03"/>

## Lesson 04 <a id="lesson-04"/>

# Table of Contents

[TOC]

# References

[^1]: "Westgrid: What We Do." [Online]. Available: <https://www.westgrid.ca/about_westgrid/what_we_do>

[^2]: "Compute Canada. Update January 11, 2017." [Online]. Available: <https://www.computecanada.ca/wp-content/uploads/2015/02/Update-January-11-2017.pdf>

[^3]: "A beginner's guide to big data terminology." [Online].  Available: <http://dataconomy.com/2016/05/a-beginners-guide-to-big-data-terminology>

[^4]: "Mini-glossary: Big data terms you should know." [Online].  Available: <http://www.techrepublic.com/article/mini-glossary-big-data-terms-you-should-know>

[^5]: "Behavioral analytics, definition by Techopedia." [Online].  Available: <https://www.techopedia.com/definition/30308/behavioral-analytics>

[^6]: "Detecting advanced threats with user behavior analytics."  [Online]. Available: <http://www.networkworld.com/article/2904356/security0/detecting-advanced-threats-with-user-behavior-analytics.html>

[^7]: "Big data definition by Tech Target." [Online]. Available: <http://searchcloudcomputing.techtarget.com/definition/big-data-Big-Data>

[^8]: "What Is Big Data?" [Online]. Available: <https://www.forbes.com/sites/lisaarthur/2013/08/15/what-is-big-data/#4fb6509b5c85>

[^9]: "Who Coined 'Cloud Computing'?" [Online]. Available: <https://www.technologyreview.com/s/425970/who-coined-cloud-computing>

[^10]: "Cloud computing: a simple introduction." [Online]. Available: <http://www.explainthatstuff.com/cloud-computing-introduction.html>

[^11]: "Data visualization definition by Tech Target." [Online].
Available: <http://searchbusinessanalytics.techtarget.com/definition/data-visualization>

[^12]: "Data visualization for human perception." [Online]. Available: <https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/data-visualization-for-human-perception>

[^13]: "Descriptive analytics definition by Tech Target." [Online]. Available: <http://whatis.techtarget.com/definition/descriptive-analytics>

[^14]: "Four Types of Big Data Analytics and Examples of Their Use."  [Online]. Available: <http://www.ingrammicroadvisor.com/data-center/four-types-of-big-data-analytics-and-examples-of-their-use>

[^15]: "Distributed file system definition by Tech Target." [Online]. Available: <http://searchwindowsserver.techtarget.com/definition/distributed-file-system-DFS>

[^16]: "Distributed file system definition by Techopedia." [Online]. Available: <https://www.techopedia.com/definition/1825/distributed-file-system-dfs>

[^17]: "A Simple Explanation Of 'The Internet Of Things'." [Online]. Available: <https://www.forbes.com/sites/jacobmorgan/2014/05/13/simple-explanation-internet-things-that-anyone-can-understand/#34e4f89b1d09>

[^18]: "Internet of things definition by Tech Target." [Online]. Available: <http://internetofthingsagenda.techtarget.com/definition/Internet-of-Things-IoT>

[^19]: "Computer network definition by Techopedia." [Online]. Available: <https://www.techopedia.com/definition/25597/computer-network>

[^20]: "What is computer networking?" [O#data-analysisnline]. Available: <https://www.lifewire.com/what-is-computer-networking-816249) [www.lifewire.com/what-is-computer-networking-816249.](https://www.lifewire.com/what-is-computer-networking-816249>

[^21]: "Social Network Analysis: An Introduction by Orgnet,LLC."  [Online]. Available: <http://www.orgnet.com/sna.html>

[^22]: "The myth of secure computing." [Online]. Available: <https://hbr.org/2003/06/the-myth-of-secure-computing) [hbr.org/2003/06/the-myth-of-secure-computing.](https://hbr.org/2003/06/the-myth-of-secure-computing>

[^23]: "Computer security definition by PC Magazine." [Online]. Available: <http://www.pcmag.com/encyclopedia/term/40169/computer-security>

[^24]: "Introduction to Structured Data, by Google." [Online]. Available: <https://developers.google.com/search/docs/guides/intro-structured-data>

[^25]: "Structured data definition by Webopedia." [Online]. Available: <http://www.webopedia.com/TERM/S/structured_data.html>

[^26]: "Unstructured data definition by Techopedia." [Online]. Available: <https://www.techopedia.com/definition/13865/unstructured-data>

[^27]: "Solving the Unstructured Data Challenge." [Online]. Available: <http://www.cio.com/article/2941015/big-data/solving-the-unstructured-data-challenge.html>

[^28]: Donoho, D. (2017). 50 years of data science. *Journal of Computational and Graphical Statistics*, *26*(4), 745-766.

[^29]:"The Data Science Venn Diagram" [Online]. Available: <http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram>

[^30]: "Introduction to Tabular Data" [Online]. Available: <https://papl.cs.brown.edu/2016/intro-tabular-data.html>

[^31]: "Tabular Database" [Online]. Available: <https://www.techopedia.com/definition/26181/tabular-database>

[^32]: "Data Modeling Introduction" [Online]. Available: <https://docs.mongodb.com/manual/core/data-modeling-introduction/>

[^33]: Greenberg, J. (2003). Metadata and the world wide web. *Encyclopedia of library and information science*, *3*, 1876-1888.

[^34]: "SQL Tutorial" [Online]. Available:  https://www.w3schools.com/sql/

[^35]: "Overview of the KDD Process" [Online]. Available: http://www2.cs.uregina.ca/~dbd/cs831/notes/kdd/1_kdd.html

[^36]: "About Text Mining" [Online]. Available: https://www.ibm.com/support/knowledgecenter/en/SS3RA7_15.0.0/com.ibm.spss.ta.help/tm_intro_tm_defined.htm

[^37]: "Introduction to Correlation" [Online]. Available: https://www.datascience.com/blog/introduction-to-correlation-learn-data-science-tutorials

[^38]: "Data vs. Information vs. Insight" [Online]. Available: https://online.ben.edu/programs/mba/resources/data-vs-information-vs-insight

[^39]: "Artificial Intelligence" [Online]. Available: https://www.techopedia.com/definition/190/artificial-intelligence-ai

[^40]: "EI-ISAC Cybersecurity Spotlight – CIA Triad" [Online]. Available: https://www.cisecurity.org/spotlight/ei-isac-cybersecurity-spotlight-cia-triad/
