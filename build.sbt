lazy val root = (project in file(".")).
  settings(
    name := "nlp-scientific-text",
    version := "1.0",
    scalaVersion := "2.11.8"
  )

resolvers ++= Seq(
  // other resolvers here
  "ScalaNLP Maven2" at "http://repo.scalanlp.org/repo",
  "Scala Tools Snapshots" at "http://scala-tools.org/repo-snapshots/",
  // if you want to use snapshot builds (currently 0.12-SNAPSHOT), use this.
  "Sonatype Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots/",
)

libraryDependencies  ++= Seq(
  // other dependencies here
  "org.scalanlp" %% "breeze" % "0.12",
  "org.scalanlp" %% "epic" % "0.3",
  "org.scalanlp" %% "english"  % "2015.1.25",
)