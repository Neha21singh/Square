from fastapi import APIRouter, Body, Request, Form, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
import uuid , json

from app.project.models import Project, ProjectUpdate

project_api = APIRouter()


#Create   
@project_api.post("/", response_description="Create a new project", status_code=status.HTTP_201_CREATED, response_model=Project)
async def create_project(request: Request, project: Project = Body(...)):
    #project = await request.json()
    #project["_id"] = str(uuid.uuid4())
    project = jsonable_encoder(project)
    #print(project)
    new_project = request.app.database["projects"].insert_one(project)
    created_project = request.app.database["projects"].find_one(
        {"_id": new_project.inserted_id}
    )

    return created_project

    
#List
@project_api.get("/", response_description="List all projects")
def list_projects(request: Request,SECTORS:str ='',BLOCKS: str =''):
    qry = {}
    if 'x-ses' in request.headers:
        # print ('FILTERING ...')
        ses = request.headers['x-ses']        
        j_ctx = json.loads(ses)
        # qry['BLOCKS'] = str(j_ctx['BLOCKS'])
    if SECTORS!='':
        qry['SECTORS'] = SECTORS
        
    if BLOCKS!='':
        qry['BLOCKS'] = BLOCKS
        
    projects = list(request.app.database["projects"].find(qry))
    return {"projects":projects}
'''   
@admin_user_api.get("/", response_description="List all user")
def list_user(request: Request,org:str='',ngo:str='',app:str='',role:str=''):
    # print('org is:',org)
    # print('ngo is:',ngo)
    # print('app is:',app)
    # print('role is:',role)

    qry = {}
    if 'x-ses' in request.headers:
        # print ('FILTERING ...')
        ses = request.headers['x-ses']        
        j_ctx = json.loads(ses)
        if (j_ctx['role'] == 'admin'): qry['ngo_id'] = str(j_ctx['ngo_id'])
    if org!='':
        qry['org_id'] = org
        
    if ngo!='':
        qry['ngo_id'] = ngo
        
    if app!='':
        qry['app_id'] = app
        
    if role!='':
        qry['role_id'] = role
    # print("er",qry)
        
    users = list(request.app.database["users"].find(qry))
    # print(users)
    return {"users":users}
'''
    
#Find
@project_api.get("/{id}", response_description="Get a single project by id", response_model=Project)
def find_project(id: str, request: Request):
    if (project := request.app.database["projects"].find_one({"_id": id})) is not None:
        return project

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with ID {id} not found")
    
#Delete
@project_api.delete("/{id}", response_description="Delete a project")
def delete_project(id: str, request: Request, response: Response):
    delete_result = request.app.database["projects"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with ID {id} not found")
    
# Update
@project_api.post("/{id}", response_description="Update a project", response_model=Project)
async def update_project(id: str, request: Request, project: ProjectUpdate = Body(...)):
    p = await request.json()
    print(p)
    
    #project = {k: v for k, v in project.dict().items() if v is not None}

    #if len(project) >= 1:
    update_result = request.app.database["projects"].update_one(
        {"_id": id}, {"$set": p}
    )

    if update_result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with ID {id} not found")

    if (
        existing_project := request.app.database["projects"].find_one({"_id": id})
    ) is not None:
        return existing_project

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with ID {id} not found")
