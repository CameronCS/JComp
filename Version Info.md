# Version Information

## Introduction
The version history is an interesting one. Generally the verion system is "x.y.z"
<table>
  <tr>
    <td>
      x
    </td>
    <td>
      New Update
    </td>
  </tr>
  <tr>
    <td>
      y
    </td>
    <td>
      Major Fix
    </td>
  </tr>
  <tr>
    <td>
      z
    </td>
    <td>
      Minor fix
    </td>
  </tr>
</table>

But for the JComp (Java Compiler System) we decided to take a different approach. We are using "w.x.y.z"
<table align="Center-align">
  <tr>
    <td>
      w
    </td>
    <td>
      The entire JComp System
    </td>
  </tr>
  <tr>
    <td>
      x
    </td>
    <td>
      The Applications version
    </td>
  </tr>
  <tr>
    <td>
      y
    </td>
    <td>
      The Major fix of the application
    </td>
  </tr>
  <tr>
    <td>
      z
    </td>
    <td>
      The Minor fix of the application
    </td>
  </tr>
</table>

## List of Files
* [JBackup](#jbackup)

* [JClean](#jclean)

* [JComp](#jcomp)

* [JCompile](#jcompile)

* [JRestore](#jrestore)

* [JRun](#jrun)

* [JRuntest](#jruntest)

## JBackup
### Introduction to JBackup
JBackup is a simple local backup system created to make local backups of your directory 

### Versions
* [Version 1.1.0.0](#version-1100)
#### Version 1.1.0.0
Version 1.1.0.0 Is the first offical release version of JBackup

It comes with the following commands
<ul>
  <li>Help</li>
  <li>Version</li>
  <li>All</li>
  <li>[filename].java</li>
</ul>

### JBackup Documentation Link
JBackup Documentation found here:
[JBackup Documentation](https://github.com/CameronCS/JComp/blob/Windows/docs/jbackup.md)

## JClean
### Introduction to JClean
JClean is a basic file file manager made to clean a directory of all `.class` files from your workspace

### Versions
* [Version 1.1.0.0](#version-1100-1)
#### Version 1.1.0.0
Version 1.1.0.0 is The first officail release of the JClean System

It comes with the following commands
<ul>
  <li>Help</li>
  <li>Version</li>
  <li>All</li>
  <li>[filename].class</li>
</ul>

### JClean Documentation Link
JClean documentation found here: 
[JClean Documentation](https://github.com/CameronCS/JComp/blob/Windows/docs/jclean.md)

## JComp
### Introduction to JComp
JComp is the main element of the JComp System which allows for the creation of java apps
### Versions
* [Version 1.1.0.0](#version-1100-2)

#### Version 1.1.0.0
Version 1.1.0.0 is the first official release of JComp

It's released with the following commands
<ul>
  <li>Help</li>
  <li>Version</li>
  <li>Create Java App</li8>
  <li>Add File</li>
  <li>Add Dir</li>
  <li>Add Files</li>
  <li>Add Dirs</li>
</ul>

### JComp Documentation Link
JComp documentation is found here: [JComp Documentation](https://github.com/CameronCS/JComp/blob/Windows/docs/jcomp.md)

## JCompile
### Introduction to JCompile
JCompile is the compile system of your java application. It creates the `.class` files for your application to run.

### Versions
* [Version 1.1.0.0](#version-1100-3)

#### Version 1.1.0.0
Version 1.1.0.0 is the first offical release version of JCompile

JCompiles release comes with the following arguments
<ul>
  <li>Help</li>
  <li>Version</li>
  <li>All</li>
  <li>[filename].java</li>
</ul>

### JCompile Documentation Link
JCompile documentation link is found here: 
[JCompile Documentation](https://github.com/CameronCS/JComp/blob/Windows/docs/jcompile.md)

## JRestore
### Introduction to JRestore
JRestore is the restoration of local backups into the main `.java` files

### Versions
* [Version 1.1.0.0](#version-1100-4)

#### Version 1.1.0.0
Version 1.1.0.0 is the first offical release of JRestore

JRestore comes with the following arguments
<ul>
  <li>Help</li>
  <li>Version</li>
  <li>All</li>
  <li>[Filename.java]</li>
</ul>

### JRestore Documentation Link
JRestore documentation link is found here: 
[JRestore Documentation](https://github.com/CameronCS/JComp/blob/Windows/docs/jrestore.md)

## JRun
### Introduction to JRun
JRun is the runner of your java application. It keeps the runtime and displays it at the end of the application run cycle.
Any file with a method: `public static void main(String[] args)` can be run as long as it is compiled

### Versions
* [Version 1.1.0.0](#version-1100-4)

#### Version 1.1.0.0
JRun comes with the functionality of not requiring any arguments
```
jrun
```
Will search for and execute the `Main.class` file by default

The following arguments that do come with jrun are
<ul>
  <li>Help</li>
  <li>Version</li>
  <li>Main</li>
  <li>[filename].java</li>
</ul>

### JRun Documentation Link
The JRun documentation link can be found here: 
[JRun Documentation](https://github.com/CameronCS/JComp/blob/Windows/docs/jrun.md)

## JRuntest
### Introduction to JRunTest
JRuntest comes with the same functionality as [JRun](#jrun), however there are no arguments required as long as the `test.class` file is in the current working directory. 

### Versions
* [Version 1.1.0.0](#version-1100-5)

#### Version 1.1.0.0
The avaliable arguments are
<ul>
  <li>Help</li>
  <li>Version</li>
</ul>

### JRuntest Documentation Link
The JRuntest documentation link can be found here: 
[JRuntest Documentation](https://github.com/CameronCS/JComp/blob/Windows/docs/jruntest.md)
