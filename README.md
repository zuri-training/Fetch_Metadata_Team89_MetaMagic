# Fetch_Metadata_Team89
# Metamagic
This is a final stage project given by Zuri to our team, Team_89, as a part of the final project phase of the Zuri training.


## Install Dependencies

1. **Python 3.10** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

- Python 3.10 upward is required

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies make sure you are on the `Fetch_Metadata_Team89_MetaMagic` directory, then run the commands below:

- **Start and activate your virtual environment**

```bash
# Mac and Linux users

python3 -m venv env
source env/bin/activate

# Windows users
> py -3 -m venv env
> env\Scripts\activate

# Windows git bash users
python3 -m venv env
source env/bin/activate
```

Run this command to install the required project dependencies e.g Django

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Django](https://www.djangoproject.com/) Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

### Set up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

After successfully setting up and installing the dependencies and setting up the database start your backend Django server by running the command below from the `/Fetch_Metadata_Team89_MetaMagic/Metamagic/` directory.

```bash
python manage.py runserver
```



## Table of contents

- Definitions
- Motivation
- Technology
- Features
- Accessibility
- How to use the project
- License



### What is Metamagic

MetaMagic is a Web platform that allows its users to upload various specified file types and extract the Metadata of those files with an option to save, export, download, share and embed in websites.

### What is Metadata?

It is data that provides information about the data. Not the content as per text or image in it self. Metadata isn’t displayed on a webpage but can be found in the pages’ code and helps search engines to understand the visible content of a webpage.

### There are many types of metadata according to wikidepia:

 #### Descriptive Metadata:
 The descriptive information about a resource. It is used for discovery and identification. It includes elements such as title, abstract, author, and  keywords.

#### Structural Metadata: 
Metadata about containers of data and indicates how compound objects  are put together, for example, how pages are ordered to form chapters. It describes the types, versions, relationships, and other characteristics of digital materials.

#### Administrative Metadata:
The information to help manage a resource, like resource type, permissions, and when and how it was created

#### Reference Metadata:
The information about the contents and quality of statistical data.

#### Statistical Metadata:
This is also called process data, may describe processes that collect, process, or produce statistical data.

#### Legal Metadata:
It provides information about the creator, copyright holder, and public licensing, if provided.


### Motivation

The Metamagic project was created to make the life of the users easy by providing an interface where they can easily get metadata information on items they upload on the platform. 


### Technology 

This project was designed on Figma, Figjam while it is built in HTML, CSS and Django.

So far it runs smoothly without any hitches in the user flow of the application.


## Features

These are some of the features of this project:

#### Upload and Generate Files:  
Metamagic allows users upload and generate metadata for specific file type in no time with just a click.

#### Download Files: 
Download generated metadata directly into any type of device you use the platform on.

#### Share Files: 
The share feature helps you share metadata anyone oniline or offline.

#### Save Files: 
Save generated metadata into the metamagic cloud for easy access. This provides you with a great record of where you have been and what you’ve done.

#### Website Embed: 
Developers get the opportunity to easily embed generated metadata into a website’s code.

#### Export Files:
The platform helps you export metadata in a text format into a folder.


### Accessibility 

In order to have full access to all the features on the platform, users must register on the platform. 
Unregistered users have limited access to the platform.

### How it runs.
This application runs on all devices as it has been built as a responsive application usable on all interfaces.

#### List of pages included in the application
- Landing Page
- Sign Up Page
- Log In Page
- Forgot Password Page
- About Us Page
- Contact Us Page
- Dashboard
- File Upload Page
- Metadata Library


### To Report An Issue

1. When you notice any issues with the code
    - Search the existing issues to find out if a similar issue has been logged by another contributor
    - If no such issues has been logged, please create a new issue. Please ensure a detailed explanation is included so that other developers will understand the issues and proffer solutions to it.
    
2. Ensure that appropriate labels are provided for easy referencing.

### Fixing An Issue

1. Search for issues you might be interested in fixing.

  - Note the tasks that requires fixing within the issue.
  
2.  For the security of the development area, fork the repository and work on the issue on your local machine.

3.  After you are through with the fix, create a pull request. Ensure there is a clear link by using an associated keyword.
  

## How To Contribute To The Project

This project is open source and you can contribute to it to make it better with all the necessary explanations, so subsequent users and contributors will understand your contributions.

#### To contribute to the project you need to do the following:

- Fork the main branch of the repository.

- Clone the forked repository to local machine.

- Set this update to ensure your repository is up to date.

- Sync changes from our repo to your forked repo.

- Pull changes from our repo to your local machine.

- Stage your changes.

- Write descriptive commit message.

- Push your changes to your remote repo.

### Pull Request

- Create a pull request on our main branch.
- Give detailed description on your pull request and link to approriate issue.
- See Fixing An Issue above.
- Wait for our reviewers to review and approve pull request for merging.

## Links

[Project Documentation](https://docs.google.com/document/d/17bwgDRxA6mNDWWl-HUSTkEuZG8i39ip3tEpNJh_AHy8/edit).


[Schema Diagram](https://drive.google.com/file/d/1OTTV7MmU-6zZtQDrFdTfvmSNHH1luR42/view?usp=sharing).


[Figma File](https://www.figma.com/file/zVCj2MJ5YTNWGJfwvUvS3P/Team_89-MetaMagic?node-id=2%3A3)



### License
=======

