from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas
from .. import oauth2
from ..database import get_db
from sqlalchemy import func
import json


router = APIRouter(
    prefix="/posts"
)


@router.get("/", response_model=List[schemas.Post])
# @router.get("/")
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    # print(limit)
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()

    posts = db.query(models.Post).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all()

    p1 = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
    # print(p1)
    # d1 = db.query(models.Vote.user_id, func.count(models.Vote.post_id).label(
    #     "votes")).group_by(models.Vote.user_id).all()
    print(posts)
    return posts
###########################################################################################################

# @router.get("/")
# @router.get("/", response_model=List[schemas.PostOut])
# def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
#               limit: int = 10, skip: int = 0, search: Optional[str] = "") -> List[dict]:
#     posts = db.query(models.Post).filter(
#         models.Post.title.contains(search)).limit(limit).offset(skip).all()
#     results = (
#         db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
#         .outerjoin(models.Vote, models.Vote.post_id == models.Post.id)
#         .group_by(models.Post.id)
#         .all()
#     )
#     # Process posts and results to prepare a JSON serializable response
#     processed_posts = [{'id': post.id, 'title': post.title} for post in posts]
#     processed_results = [{'post_id': post.id, 'votes': votes}
#                     for post, votes in results]
#     data = processed_posts + processed_results
#     # json_string = json.dumps(data)
#     # print(json_string)
#     return data
###########################################################################################################
# @routers.post("/posts")
# def created_posts():
#     print("post")
#     # print(post.dict())
#     return {"data":"test"}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s ,%s) RETURNING *""",
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # print(current_user.id)
    # print(current_user.email)
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
# titel str, cotent str, category,bool published


# @routers.get("/posts/latest")
# def get_letest_post():
#     post = my_posts[len(my_posts)-1]
#     return post

######################################################################################################
@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, response: Response,  db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
    #    print(post)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="post wit id: {id} was not found")

    return post

###############################################################################################################


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delelet_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #     """DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    # delelet_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id}dose not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="not authorized to perfrom requested acction")
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

###########################################################################################################


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, update_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    #                (post.title, post.content, post.published, (str(id))))

    # updated_post = cursor.fetchone()
    # conn.commit()

    Post_query = db.query(models.post).filter(models.post.id == id)
    post = Post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id}dose not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="not authorized to perfrom requested acction")

    Post_query.update(update_post.dict(), synchronize_session=False)

    db.commit()

    return Post_query.first()
