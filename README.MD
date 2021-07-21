## 2021-064 (Lecture Video/Audio quality Enhancer)

### How to set up for development
1. Install latest [Anaconda](https://www.anaconda.com/products/individual) (current = conda 4.9.2) on your PC.
2. Clone the repo `http://gitlab.sliit.lk/2021-064/2021-064.git`.
3. Create conda environment as `SLIIT-2021-064`.\
    `conda create -n SLIIT-2021-064 python=3.8`
4. Open PyCharm and open project folder.
5. Check whether you are in `SLIIT-2021-064` conda environment in pyCharm terminal. If not, activate conda env by running \
   `conda activate SLIIT-2021-064`.
6. When you are in `SLIIT-2021-064` conda env, run
    `pip install -r requirements.txt` at project root directory.
   
7. Install tesseract-ocr according to this page. Link:https://tesseract-ocr.github.io/tessdoc/Installation.html
8. Install pytesseract inside the conda environment according to this page. Link:https://anaconda.org/conda-forge/pytesseract

### Guidelines
📌Donot use `requirements.txt` with pip. Use it only to manually add records of new libraries installing. \
📌After installing a new library, do `pip freeze >  requirements2.txt` and commit the change happened in the `requirements2.txt`.

### How to make a build
//TODO
### How to test
//TODO
### Main objective
Create a video editor to enhance video and audio quality and experience of lecture recordings.
### Main Research questions
Usually lecture recordings have many problems like long duration, unclear audio, monotonous audio, irrelevant video parts.
### Individual research question & Objectives
* #### IT18117110 (Jayawardana N.S) - Leader
    * ##### Research Question
      &nbsp;&nbsp;&nbsp;&nbsp; In many lecture recordings, the voice of the lecturer is not expressive like the voice of a public speaker.
      Less expressive monotonous voices are usually hard to understand by humans.
    * ##### Objective
      &nbsp;&nbsp;&nbsp;&nbsp; There have been studies on what makes a Charismatic speaker. It has found that prosodic attributes such as varying the pitch between low and high, varying a length of an utterance, varying the loudness between soft and loud helps to make charismatic impact. In this research how to apply pitch and loudness variances while changing the length for each utterance will be studied and implemented as following.
      In this project a Tkinter-python desktop application will be implemented which do topic modelling processes, apply prosodic modifiers to topic words, and communicates with resemble.ai (capable of voice cloning and synthesizing speech with prosodic changes) to generate a more expressive audio for the lecture recording.
      The co-relation between topic modelling based prosodic modifications and overall expressiveness of the generated audio will be evaluated.
* #### IT18117356 ( Bandara A.B.C.N)
    * ##### Research Question
      &nbsp;&nbsp;&nbsp;&nbsp; At present most universities provide online lectures to students. The problem is lecturers are not professional video editors. Most of them do not edit the videos even when they do, they have to spend a long time doing it. Even then there can be many mistakes. Because of that, students receives low-quality content. It is crucial to have high-quality content to maintain students’ motivation throughout the lecture.
    * ##### Objective
      &nbsp;&nbsp;&nbsp;&nbsp; The objective is to create a desktop application that can analyze the video content. The application checks If each slide has too many sentences and the lecturer's face and eyes are not visible in the video then alerts the lecturer to show the timestamps. With the timestamps, the lecturer can re-record low-quality parts and edit the video.
* #### IT18120844 (Dissanayake D.M.T.C)
    * ##### Research Question
      &nbsp;&nbsp;&nbsp;&nbsp;Once a webinar is recorded, If the question statements of the video can be extracted, and suggest answers, it is a great convenient for students.
      
    * ##### Objective
      &nbsp;&nbsp;&nbsp;&nbsp; 
        The system automatically identifies the questions which are  specific  to  the  related  domain.Students  can  get  a  downloadable  document including all questions and answers which were asked during the lectures, and it will be much helpful to ready for the exams as well. This document contains answers total questions and explanations. Additionally, in student preview (a preview somewhat like lecturecapture.sliit.lk),  students  can  move  to  the  exact  position  of  the  question  by clicking the question in the side window.Suggested answers for the questions are also be displayed in a window.
* #### IT18134490 (Fernando  M.M.P.J.R)
    * ##### Research Question
      &nbsp;&nbsp;&nbsp;&nbsp; 
      When using a video editor to edit video, lectures most of the time is editing the unwanted parts to be removed from the lecture video. For lectures, it takes time to edit and still after editing there can be places that need to be edited. If the video editor can automatically tell the unwanted places that need to be edited it make the time less to edit the video and there won’t be any places that have been not edited.by doing so the length of the video can be also reduced it will be useful to student and lecture both. 
        In lectures there are part that students do not know if it is important to look at because of that student some time mise some main points given by the lecture if the student would know that the point that lecture is saying is an important point it would be useful for the students that are watching the lecture video.

    * ##### Objective
      &nbsp;&nbsp;&nbsp;&nbsp; 
        Removal of no-movement/blank screen parts with no-speaking parts and video zoom-in functionality.
### Other necessary information 
* Supported platforms
  * Windows 10
  * macOS
    
### Authors
* IT18117110 (Jayawardana N.S) - Leader
* IT18117356 (Bandara A.B.C.N)
* IT18120844 (Dissanayake D.M.T.C )
* IT18134490 (Fernando  M.M.P.J.R)

### Supervisors
* Dr. Nuwan Kodagoda
* Mrs. Kushnara Suriyawansa