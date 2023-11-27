# import json

# @router.get("/")
# @router.get("/", response_model=List[schemas.Post])
# def get_posts(db: session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
#               limit: int = 10, skip: int = 0, search: Optional[str] = "") -> List[dict]:
#     posts = db.query(models.Post).filter(
#         models.Post.title.contains(search)).limit(limit).offset(skip).all()
#     results = (
#         db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
#         .outerjoin(models.Vote, models.Vote.post_id == models.Post.id)
#         .group_by(models.Post.id)
#         .all()
#     )
# Process posts and results to prepare a JSON serializable response
# processed_posts = [{'id': post.id, 'title': post.title} for post in posts]
# processed_results = [{'post_id': post.id, 'votes': votes}
#                      for post, votes in results]
# data = processed_posts + processed_results
# json_string = json.dumps(data)
# print(json_string)
# return data
###################################################################





 # results = (
    # db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
    # .outerjoin(models.Vote, models.Vote.post_id == models.Post.id)
    # .group_by(models.Post.id)
    # .all()
    #                 )







##############
# def upgrade():
#     op.add_column('posts', sa.Column(
#         'owner_id', sa.Integer(), nullable=False))


#     op.create_foreign_key('post_users_fk', source_table="posts",
#                       referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
# pass


# def downgrade():
#     op.drop_constraint('post_users_fk', table_name="posts")


#     op.drop_column('posts', 'owner_id')
# pass

#################

# def upgrade(): op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
#                                                   primary_key=True), sa.Column('title', sa.String(), nullable=False))
# pass


# def downgrade() -> None:
#     pass

# ##################


# def upgrade():op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
# pass


# def downgrade():op.drop_column('posts','content')
# pass

######################
# def upgrade(): op.create_table('users', sa.Column('id', sa.Integer, nullable=False),
#                                sa.Column('email', sa.String(), nullable=False),
#                                sa.Column('password', sa.String(),
#                                          nullable=False),
#                                sa.Column('created_at', sa.TIMESTAMP(timezone=True),
#                                          server_default=sa.text('now()'), nullable=False),
#                                sa.PrimaryKeyConstraint('id'),
#                                sa.UniqueConstraint('email')
#                                )


# pass


# def downgrade(): op.drop_table('users')


# pass

#######################

# def upgrade():
#     op.add_column('posts', sa.Column('published', sa.Boolean(),
#                   nullable=True, server_default='TRUE'),)


#     op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
#                   timezone=True), nullable=False, server_default=sa.text('NOW()')),)
# pass


# def downgrade():
#     op.drop_column('posts', 'published')
#     op.drop_column('posts', 'created_at')


# pass