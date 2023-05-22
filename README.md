# __fastApi__ 

##   <p> Metal Price </p>


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmiro.medium.com%2Fmax%2F1023%2F1*du7p50wS_fIsaC_lR18qsg.png&f=1&nofb=1" style="width:600px;"/>


---

## * Set-Up
* Install virtual enviroment
  *  > ### sudo apt install python3.8-venv
---
* Create virtual enviroment
   * > ### python3 -m venv env
---
* Move inside virtual enviroment
   * > ### source TestNote/bin/activate
---
* Exite virtual enviroment
    * > ### deactivate
---
* Install requirement
    * > ### pip3 install -r requirements.txt
---
* Create dir "Learner" (contain **working files**) ,add move 
    * > ### mkdir "< file_dir >"
    * > ### cd "< file_dir >"

---
## Role of Code

* Create file **main.py** in Learner dir
    * code...
---
* Start server
    * > ### uvicorn main:app --reload
    * ### Swagger-UI
        * <u>http://127.0.0.1:8000/docs</u>
---
