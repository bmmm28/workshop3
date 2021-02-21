from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()

# http method [ get, post, put, patch, delete ]
# command database [ find, insert, update, update, delete ]


@app.get("/")
def index():
    return JSONResponse(content={"message": "Hello,  World"}, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)

    """

@app.get("/profiles/{name}")  #path#
def get_query_parameter(name: str):
	return JSONResponse(
		content={"message": f"My name is: {name}"},
		status_code=200,
)

************************************************************************************
@app.get("/profiles/")
def get_query_parameter(start: int = 0, limit: int = 0): # query_parameter กำหนด default value --> int รับค่าจาก url ///start=28&limit=10
	return JSONResponse(
		content={"message": f"profile start: {start} limit: {limit}"},
		status_code=200,
)

************************************************************************************
@app.get("/books") /// ชื่อหนังสือทั้งหมดใน db ควรตั้งชื่อ path ตามชื่อหัวตารางใน db
def get_books():
	#v  query มาจาก database 
    dict_books = [
	{
		"book_id": 1,
		"book_name": "Harry Potter and Philosopher's Stone",
		"page": 223,
	},
	{
		"book_id": 2,
		"book_name": "Harry Potter and the Chamber of Secrets",
		"page": 251,
	},
	{
		"book_id": 3,
		"book_name": "Harry Potter and Prisoner of Azkaban",
		"page": 251,
	}
]

	return JSONResponse(content={"status": "ok", "data": dict_books},status_code=200)

***************************************************************************************
@app.get("/books/{book_id}") # แสดงชื่อหนังสือตาม id ที่กรอก ex. /books/5 #select * from books where id = book_id
def get_books_by_id(book_id: int):
	book = {
		"book_id": 1,
		"book_name": "Harry Potter and Philosopher's Stone",
		"page": 223,
	}
	resonse = {"status": "ok", "data": book}

	return JSONReponse(content = response, status_code=200)

****************************************************************************************
				
			--------------create-------------

class createBookPayload(BaseModel):
	id: str
	name: str
	page: int

****************************************************************************************
@app.post("/books")
def create_books(req_body: createBookPayload):
	req_body_dict = req_body.dict()
	id = req_body_dict["id"]
	name = req_body_dict["name"]
	page = req_body_dict["page"]
	book = {
		"id": id,
		"name": name,
		"page": page,
	}
	response = {"status": "ok", "data": book}
	return JSONResponse(content = response, satatus_code=201)

*****************************************************************************************

			----------------update---------------

class updateBookPayload(BaseModel):
	name: str
	page: int

*****************************************************************************************
@app.patch("/books/{book_id}")
def update_book_by_id(req_body: updateBookPayload, book_id: str):
	req_body_dict = req_body.dict()

	name = req_body_dict["name"]
	page = req_body_dict["page"]

	print(f"name: {name}, page: {page}")

	update_message = f"Update book id {book_id} is complete !!"
	response = {"status": "ok", "data": update_message}
	return JSONResponse(content=response, status_code=200)

*****************************************************************************************

			----------------delete-------------

@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: int):
	delete_message = f"Delete book id {book_id} is complete !!"
	response = {"status": "ok", "data": delete_message}
	return JSONResponse(content=response, status_code=200) 
    """
