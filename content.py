"""Content for the personal homepage. Edit values here to update the site."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Profile:
    name: str
    title: str
    affiliations: tuple[str, ...]
    location: str
    github: str
    linkedin: str
    email: str
    whoami: str


@dataclass(frozen=True)
class Project:
    name: str
    org: str
    description: str
    url: str
    role: str = ""  # GitHub stars are fetched live via shields.io in the template


@dataclass(frozen=True)
class Talk:
    title: str
    venue: str
    year: str
    url: str = ""
    summary: str = ""
    co_presenters: str = ""
    # Optional human-readable date, e.g. "Jun 10, 2025". Falls back to year.
    date: str = ""


@dataclass(frozen=True)
class BlogPost:
    title: str
    date: str  # YYYY-MM-DD or YYYY-MM
    url: str
    summary: str = ""
    venue: str = "Databricks"


@dataclass(frozen=True)
class DiveSite:
    region: str
    country: str
    lat: float
    lon: float
    kind: str  # "freedive" or "scuba"
    note: str = ""


PROFILE = Profile(
    name="Hyukjin Kwon",
    title="Staff Software Engineer, Databricks",
    affiliations=(
        "Apache Software Foundation Member",
        "Apache Spark PMC member",
        "Apache Spark Committer",
        "Freediver Instructor, PADI",
    ),
    location="Seoul, South Korea",
    github="HyukjinKwon",
    linkedin="hyukjin-kwon-25045412b",
    email="gurwls223@apache.org",
    whoami=(
        "Staff SWE at Databricks and tech-lead for the open-source PySpark team. "
        "Apache Spark PMC member and committer. Working on PySpark, Spark Connect, "
        "the pandas API on Spark, and the development infrastructure that keeps the "
        "project healthy. Also a PADI Freediver Instructor."
    ),
)

# Long-form bio for the About page. Each list item becomes a paragraph.
# HTML is allowed (rendered with the `safe` filter).
ABOUT_BIO: list[str] = [
    "I'm a Staff Software Engineer at Databricks and tech-lead for the "
    "open-source PySpark team. I've spent most of the last decade working on "
    "Apache Spark, primarily PySpark, Spark SQL, SparkR, and the development "
    "infrastructure that keeps the project healthy. I'm an Apache Software "
    "Foundation member and a PMC member and committer on Apache Spark.",

    "I came to the Spark ecosystem by way of Hortonworks and Cloudera, where "
    "I worked on the Hive and Spark integration before joining Databricks. "
    "Before that, I was a senior computer engineer at MOBIGEN in Seoul, and "
    "earlier I interned at LG Electronics. I studied at UCL "
    "(MSc, Information Science).",

    "Most of my work centers on making PySpark feel like a first-class "
    "Python library 🐍: <strong>Pandas UDFs</strong> and Python type hints, "
    "Arrow-optimized Python UDFs, the <strong>pandas API on Spark</strong>, "
    "and the Python side of <strong>Spark Connect</strong>. I led "
    "<strong>Project Zen</strong>, the broader push to make PySpark more "
    "Pythonic, and have co-authored most of the Apache Spark release "
    "announcements on the Databricks blog.",

    "In 2022, Apache Spark received the "
    "<a href=\"https://sigmod.org/2022-sigmod-systems-award/\">ACM SIGMOD "
    "Systems Award</a> 🏆, recognizing the project as \"an innovative, widely-used, "
    "open-source, unified data processing system encompassing relational, "
    "streaming, and machine-learning workloads.\" I'm one of the contributors "
    "named in the award.",

    "Outside of code, I'm a <strong>PADI Freediver Instructor</strong> 🤿 and "
    "teach students on a freelance basis around Seoul. I dive scuba too, with "
    "logged dives across Korea, Taiwan, Thailand, Vietnam, the Philippines, "
    "Indonesia, the Maldives, Saipan, and Guam. Apnea and software "
    "engineering have less in "
    "common than you'd think. Both reward calm under uncomfortable "
    "conditions, and both punish you for trying too hard.",
]

PROJECTS: list[Project] = [
    Project(
        name="spark",
        org="apache",
        description="A unified analytics engine for large-scale data processing.",
        url="https://github.com/apache/spark",
        role="PMC member, committer",
    ),
    Project(
        name="arrow",
        org="apache",
        description=(
            "Universal columnar format and multi-language toolbox for fast "
            "data interchange."
        ),
        url="https://github.com/apache/arrow",
        role="Contributor",
    ),
    Project(
        name="py4j",
        org="py4j",
        description="Enables Python programs to dynamically access arbitrary Java objects.",
        url="https://github.com/py4j/py4j",
        role="Maintainer",
    ),
    Project(
        name="koalas",
        org="databricks",
        description=(
            "Pandas API on Apache Spark. Co-led; merged upstream into PySpark "
            "as the pandas-on-Spark API in Spark 3.2."
        ),
        url="https://github.com/databricks/koalas",
        role="Co-lead / core contributor",
    ),
    Project(
        name="spark-xml",
        org="databricks",
        description="XML data source for Spark SQL and DataFrames.",
        url="https://github.com/databricks/spark-xml",
        role="Original author",
    ),
]

# Conference talks and recorded sessions. Newest first.
TALKS: list[Talk] = [
    Talk(
        title="No-Code Change in Your Python UDF for Arrow Optimization",
        venue="Data + AI Summit 2025",
        year="2025",
        date="Jun 10, 2025",
        url="https://www.youtube.com/watch?v=vslunJeDnDI",
        summary=(
            "How Arrow-optimized Python UDFs in Apache Spark deliver large "
            "speedups for existing Python UDFs without any user code change."
        ),
    ),
    Talk(
        title="아무것도 안고치고 Python UDF 2배 빠르게 만들기",
        venue="Data Intelligence Day 2025",
        year="2025",
        date="Apr 29, 2025",
        url="https://vimeo.com/1085919589",
        summary=(
            "Korean-language talk. Make your Python UDF 2x faster without "
            "changing anything: Arrow-optimized Python UDFs in Apache Spark."
        ),
    ),
    Talk(
        title="Profile, debug and monitor my PySpark workloads",
        venue="PyCon APAC 2024",
        year="2024",
        date="Oct 26, 2024",
        url="https://www.youtube.com/watch?v=jWp_U_JwU2k",
        summary=(
            "How to profile, debug, and monitor PySpark workloads in "
            "distributed environments using cProfile, the Spark UI, and "
            "observable streaming metrics."
        ),
    ),
    Talk(
        title="How do I debug my PySpark workloads?",
        venue="PyCon Hong Kong",
        year="2024",
        url="https://www.youtube.com/watch?v=Ar3lPI_MBsU",
        summary=(
            "Practical methods for debugging and profiling PySpark applications "
            "in distributed environments using cProfile and other standard tools."
        ),
        co_presenters="Allison Wang",
    ),
    Talk(
        title="Demystifying pandas with PySpark when scaling out",
        venue="PyData Vermont 2024",
        year="2024",
        date="Jul 29, 2024",
        url="https://www.youtube.com/watch?v=Ff78Y6FXIkw",
        summary=(
            "Walking through how to scale pandas workloads with the "
            "pandas-on-Spark API in PySpark, what changes for distributed "
            "execution, and the practical pitfalls when moving from local "
            "pandas to a Spark cluster."
        ),
    ),
    Talk(
        title="Dependency Management in Spark Connect: Simple, Isolated, Powerful",
        venue="Data + AI Summit 2024",
        year="2024",
        date="Jun 12, 2024",
        url="https://www.youtube.com/watch?v=PbvIak6Z8eI",
        summary=(
            "How Spark Connect simplifies dependency management in distributed "
            "environments, by packaging and updating custom Python and Scala "
            "environments per session."
        ),
        co_presenters="Akhil Gudesa",
    ),
    Talk(
        title="오픈소스로 시작해서 실리콘밸리까지",
        venue="Databricks",
        year="2024",
        date="Apr 23, 2024",
        url="https://www.youtube.com/watch?v=QbDpdjSWnmI",
        summary=(
            "Korean-language talk. From open source to Silicon Valley: career "
            "path through Apache Spark and how OSS contributions led to "
            "Databricks."
        ),
    ),
    Talk(
        title="Scaling pandas to any size with PySpark",
        venue="EuroSciPy 2023, Switzerland",
        year="2023",
        date="Aug 17, 2023",
        url="https://www.youtube.com/watch?v=HRiawu8k7dU",
        summary=(
            "Scaling pandas workloads to arbitrary data sizes using the "
            "pandas API on Spark in PySpark."
        ),
    ),
    Talk(
        title="pandas와 PySpark로 데이터 워크로드 확장하기",
        venue="PyCon Korea 2023, South Korea",
        year="2023",
        date="Aug 12, 2023",
        url="https://www.youtube.com/watch?v=Rpsf61z4uNw",
        summary=(
            "Korean-language talk at PyCon Korea 2023. Scaling data workloads "
            "with pandas and PySpark."
        ),
    ),
    Talk(
        title="Python with Spark Connect",
        venue="Data + AI Summit 2023, San Francisco",
        year="2023",
        date="Jun 29, 2023",
        url="https://www.youtube.com/watch?v=QGUvjcrqj-U",
        summary=(
            "Using Python with Spark Connect, the decoupled client/server "
            "architecture introduced in Spark 3.4, and the developer-experience "
            "improvements it enables."
        ),
    ),
    Talk(
        title="Lakehouse / Spark AMA",
        venue="Data + AI Summit 2023, San Francisco",
        year="2023",
        date="Jun 29, 2023",
        url="https://www.youtube.com/watch?v=ngi8eyK9M0Q",
        summary=(
            "Live AMA covering Apache Spark, Spark Connect, and the lakehouse "
            "architecture with several Spark committers."
        ),
    ),
    Talk(
        title="Scaling data workloads using the best of both worlds: pandas and Spark",
        venue="PyData Seattle 2023",
        year="2023",
        date="Jun 20, 2023",
        url="https://www.youtube.com/watch?v=knxbfJuC67I",
        summary=(
            "How to combine pandas and PySpark idiomatically to scale data "
            "analysis workloads, with implementation details and best-practice "
            "guidance for analysts and scientists."
        ),
        co_presenters="Chengyin Eng",
    ),
    Talk(
        title="Spark Connect로 어디서든 쉽게 원격으로 PySpark 사용하기",
        venue="Databricks",
        year="2023",
        date="Apr 25, 2023",
        url="https://www.youtube.com/watch?v=RsVJjeE-5K0",
        summary=(
            "Korean-language talk. Easily use PySpark remotely from anywhere "
            "with Spark Connect."
        ),
    ),
    Talk(
        title="PySpark in Apache Spark 3.3 and Beyond",
        venue="Data + AI Summit 2022, San Francisco",
        year="2022",
        date="Jun 29, 2022",
        url="https://www.youtube.com/watch?v=IVMpVOg1-NY",
        summary=(
            "PySpark improvements in Spark 3.3 and the roadmap ahead: default "
            "index support for the pandas API, type hints in source, UDF "
            "profiler, and upcoming Structured Streaming and Arrow work."
        ),
        co_presenters="Xinrong Meng",
    ),
    Talk(
        title="Databricks Korea Lakehouse Day 2022",
        venue="Databricks",
        year="2022",
        date="Apr 20, 2022",
        url="https://www.youtube.com/watch?v=S4cIYj3P_co&t=3499",
    ),
    Talk(
        title="Project Zen: Making Data Science Easier in PySpark",
        venue="Data + AI Summit 2021, San Francisco",
        year="2021",
        date="May 26, 2021",
        url="https://www.youtube.com/watch?v=9HqJ0H7lAd4",
        summary=(
            "Project Zen: making PySpark more Pythonic with better docs, type "
            "hints, error messages, and pandas interoperability."
        ),
    ),
    Talk(
        title="Pandas UDF and Python Type Hint in Apache Spark 3.0",
        venue="Spark + AI Summit 2020",
        year="2020",
        date="Jun 24, 2020",
        url="https://youtu.be/UZl0pHG-2HA",
        summary=(
            "Introducing the redesigned Pandas UDF API in Spark 3.0: type "
            "hints, the new Pandas Function API, and the rationale for the "
            "redesign."
        ),
    ),
    Talk(
        title="Vectorized R Execution in Apache Spark",
        venue="Spark AI Summit 2019 EUROPE",
        year="2019",
        date="Oct 16, 2019",
        url="https://youtu.be/3fE9MrV7uqA",
        summary=(
            "Vectorization in Apache Spark: Arrow-based columnar exchange, "
            "Pandas UDFs, and the SparkR performance work that brought "
            "vectorized gapply / dapply and DataFrame I/O to SparkR."
        ),
    ),
    Talk(
        title="What's New in Apache Spark 2.3 and Spark 2.4",
        venue="Dataworks 2019, Singapore",
        year="2018",
        date="Oct 11, 2018",
        url="https://www.slideshare.net/Hadoop_Summit/whats-new-in-apache-spark-23-and-spark-24",
        summary=(
            "Walkthrough of Spark 2.3 and 2.4 highlights: Data Source API V2, "
            "vectorized ORC reader, Pandas UDFs, continuous Structured "
            "Streaming, Kubernetes support, and barrier execution mode."
        ),
    ),
]

# Databricks blog posts authored / co-authored. Sorted newest first.
BLOG_POSTS: list[BlogPost] = [
    BlogPost(
        title="Databricks Lakeguard: Supporting Fine-Grained Access Control and Multi-User Capabilities for Apache Spark Workloads",
        date="2025-06",
        url="https://dl.acm.org/doi/10.1145/3722212.3724433",
        summary="SIGMOD 2025 industry paper. Describes the unified governance system that uses Spark Connect as a JDBC-like execution protocol to separate client applications from the Spark server, enforce fine-grained access policies, and isolate user code within the cluster manager.",
        venue="SIGMOD 2025 (paper)",
    ),
    BlogPost(
        title="Introducing Apache Spark 4.1",
        date="2025-12-22",
        url="https://www.databricks.com/blog/introducing-apache-sparkr-41",
        summary="Apache Spark 4.1 in Databricks Runtime 18.0 Beta: Spark Declarative Pipelines, Real-Time Mode for streaming, PySpark improvements.",
    ),
    BlogPost(
        title="Introducing Apache Spark 4.0",
        date="2025-05-28",
        url="https://www.databricks.com/blog/introducing-apache-spark-40",
        summary="Spark 4.0 in DBR 17.0: Spark Connect multi-language clients (Go, Swift, Rust), VARIANT type, Python improvements.",
    ),
    BlogPost(
        title="PySpark in 2023: A Year in Review",
        date="2024-03-25",
        url="https://www.databricks.com/blog/pyspark-2023-year-review",
        summary="Recap of PySpark in 2023: Spark Connect, Arrow-optimized UDFs, English SDK, the PySpark test framework.",
    ),
    BlogPost(
        title="Parameterized queries with PySpark",
        date="2024-01-03",
        url="https://www.databricks.com/blog/parameterized-queries-pyspark",
        summary="Parameterized SQL query API in PySpark for safer, more reusable SQL templates that prevent injection.",
    ),
    BlogPost(
        title="Python Dependency Management in Spark Connect",
        date="2023-11-14",
        url="https://www.databricks.com/blog/python-dependency-management-spark-connect",
        summary="Managing per-session Python dependencies in Spark Connect with virtualenv and conda archives.",
    ),
    BlogPost(
        title="Arrow-optimized Python UDFs in Apache Spark 3.5",
        date="2023-11-06",
        url="https://www.databricks.com/blog/arrow-optimized-python-udfs-apache-sparktm-35",
        summary="Apache Arrow-based serialization speeds up regular Python UDFs in Spark 3.5 and DBR 14.0.",
    ),
    BlogPost(
        title="Introducing Apache Spark 3.5",
        date="2023-09-15",
        url="https://www.databricks.com/blog/introducing-apache-sparktm-35",
        summary="Spark Connect GA in Scala, DeepSpeed distributor, RocksDB improvements, PySpark error class migration.",
    ),
    BlogPost(
        title="Spark Connect Available in Apache Spark 3.4",
        date="2023-04-18",
        url="https://www.databricks.com/blog/2023/04/18/spark-connect-available-apache-spark.html",
        summary="Introduces the decoupled client/server Spark Connect architecture shipping in Spark 3.4.",
    ),
    BlogPost(
        title="Introducing Apache Spark 3.4 for Databricks Runtime 13.0",
        date="2023-04-14",
        url="https://www.databricks.com/blog/2023/04/14/introducing-apache-sparktm-34-databricks-runtime-130.html",
        summary="Spark 3.4 in DBR 13.0: Spark Connect, PyTorch distributor, pandas 2.0 support.",
    ),
    BlogPost(
        title="Python Arbitrary Stateful Processing in Structured Streaming",
        date="2022-10-18",
        url="https://www.databricks.com/blog/python-arbitrary-stateful-processing-structured-streaming",
        summary="applyInPandasWithState for arbitrary stateful streaming aggregations in PySpark.",
    ),
    BlogPost(
        title="Introducing Apache Spark 3.3 for Databricks Runtime 11.0",
        date="2022-06-15",
        url="https://www.databricks.com/blog/2022/06/15/introducing-apache-spark-3-3-for-databricks-runtime-11-0.html",
        summary="Spark 3.3 in DBR 11.0: row-level Bloom filters and broader pandas API coverage.",
    ),
    BlogPost(
        title="How to Monitor Streaming Queries in PySpark",
        date="2022-05-27",
        url="https://www.databricks.com/blog/2022/05/27/how-to-monitor-streaming-queries-in-pyspark.html",
        summary="Using PySpark's Observable API to ship Structured Streaming metrics to external monitoring systems.",
    ),
    BlogPost(
        title="Introducing Apache Spark 3.2",
        date="2021-10-19",
        url="https://www.databricks.com/blog/2021/10/19/introducing-apache-spark-3-2.html",
        summary="Spark 3.2 in DBR 10.0: pandas API on Spark, ANSI SQL improvements, RocksDB state store.",
    ),
    BlogPost(
        title="Pandas API on Apache Spark 3.2",
        date="2021-10-04",
        url="https://www.databricks.com/blog/2021/10/04/pandas-api-on-upcoming-apache-spark-3-2.html",
        summary="Koalas merged into PySpark as the official pandas API on Spark in 3.2.",
    ),
    BlogPost(
        title="Benchmark: Koalas (PySpark) and Dask",
        date="2021-04-07",
        url="https://www.databricks.com/blog/2021/04/07/benchmark-koalas-pyspark-and-dask.html",
        summary="Koalas vs Dask benchmark: roughly 4 to 25 times faster than Dask depending on workload.",
    ),
    BlogPost(
        title="Introducing Apache Spark 3.1",
        date="2021-03-02",
        url="https://www.databricks.com/blog/2021/03/02/introducing-apache-spark-3-1.html",
        summary="Spark 3.1 in DBR 8.0: Python usability, ANSI SQL, query optimizer improvements.",
    ),
    BlogPost(
        title="How to Manage Python Dependencies in PySpark",
        date="2020-12-22",
        url="https://www.databricks.com/blog/2020/12/22/how-to-manage-python-dependencies-in-pyspark.html",
        summary="Shipping Python packages with PySpark jobs via PEX, conda-pack, and venv-pack archives.",
    ),
    BlogPost(
        title="An Update on Project Zen: Improving Apache Spark for Python Users",
        date="2020-09-04",
        url="https://www.databricks.com/blog/2020/09/04/an-update-on-project-zen-improving-apache-spark-for-python-users.html",
        summary="Project Zen update: PySpark docs redesign, type hints, classified error handling, install profiles.",
    ),
    BlogPost(
        title="Interoperability between Koalas and Apache Spark",
        date="2020-08-11",
        url="https://www.databricks.com/blog/2020/08/11/interoperability-between-koalas-and-apache-spark.html",
        summary="Interchanging data and operations between Koalas DataFrames and PySpark DataFrames.",
    ),
    BlogPost(
        title="A Comprehensive Look at Dates and Timestamps in Apache Spark 3.0",
        date="2020-07-22",
        url="https://www.databricks.com/blog/2020/07/22/a-comprehensive-look-at-dates-and-timestamps-in-apache-spark-3-0.html",
        summary="How to effectively use dates and timestamps in Spark 3.0: calendars, time zones, and the proleptic Gregorian switch.",
    ),
    BlogPost(
        title="Koalas 1.0: Scale Pandas with Apache Spark",
        date="2020-06-24",
        url="https://www.databricks.com/blog/2020/06/24/introducing-koalas-1-0.html",
        summary="Koalas 1.0 with about 80 percent pandas API coverage, Spark 3.0 support, new Spark accessor.",
    ),
    BlogPost(
        title="Vectorized R I/O in Upcoming Apache Spark 3.0",
        date="2020-06-01",
        url="https://www.databricks.com/blog/2020/06/01/vectorized-r-i-o-in-upcoming-apache-spark-3-0.html",
        summary="Arrow-based vectorization for SparkR gapply, dapply, and DataFrame I/O in Spark 3.0.",
    ),
    BlogPost(
        title="New Pandas UDFs and Python Type Hints in the Upcoming Release of Apache Spark 3.0",
        date="2020-05-20",
        url="https://www.databricks.com/blog/2020/05/20/new-pandas-udfs-and-python-type-hints-in-the-upcoming-release-of-apache-spark-3-0.html",
        summary="Redesigned Pandas UDF API built on Python type hints for clearer, more Pythonic UDFs.",
    ),
    BlogPost(
        title="10 Minutes from pandas to Koalas on Apache Spark",
        date="2020-03-31",
        url="https://www.databricks.com/blog/2020/03/31/10-minutes-from-pandas-to-koalas-on-apache-spark.html",
        summary="Quick-start tutorial mapping common pandas operations to their Koalas equivalents.",
    ),
    BlogPost(
        title="Integrating Apache Hive with Apache Spark - Hive Warehouse Connector",
        date="2018-10-03",
        url="https://community.cloudera.com/t5/Community-Articles/Integrating-Apache-Hive-with-Apache-Spark-Hive-Warehouse/ta-p/249035",
        summary="The Hive Warehouse Connector for reading and writing data between Spark and Hive.",
        venue="Cloudera Community (formerly Hortonworks)",
    ),
]

NAV_LINKS: list[tuple[str, str]] = [
    ("/", "home"),
    ("/about/", "about"),
    ("/projects/", "projects"),
    ("/talks/", "talks"),
    ("/writing/", "writing"),
    ("/diving/", "diving"),
    ("/contact/", "contact"),
]

# Approximate dive locations transcribed from the dive log map screenshot.
# Region-level pins by default (not precise sites) for privacy.
DIVE_SITES: list[DiveSite] = [
    DiveSite("Busan", "South Korea", 35.18, 129.08, "freedive"),
    DiveSite("Green Island (Lyudao)", "Taiwan", 22.66, 121.50, "scuba"),
    DiveSite("Phuket / Andaman Sea", "Thailand", 7.88, 98.39, "scuba"),
    DiveSite("Similan Islands", "Thailand", 8.65, 97.65, "freedive"),
    DiveSite("Phu Quoc", "Vietnam", 10.22, 103.96, "scuba"),
    DiveSite("Maldives", "Maldives", 4.18, 73.51, "scuba"),
    DiveSite("Cebu / Visayas", "Philippines", 10.32, 123.90, "freedive"),
    DiveSite("Bali", "Indonesia", -8.34, 115.09, "freedive"),
    DiveSite("Lombok / Komodo area", "Indonesia", -8.65, 117.50, "freedive"),
    DiveSite("Saipan", "Northern Mariana Islands", 15.18, 145.75, "scuba"),
    DiveSite("Guam", "Guam", 13.44, 144.79, "scuba"),
]
