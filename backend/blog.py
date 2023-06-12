
# MODEL SERIALIZER
blog_model = api.model(
    "Blog",
    {
        "id": fields.Integer(),
        "title": fields.String(),
        "content": fields.String(),
        "created_at": fields.DateTime()
    }
)

@api.route('/blogs')
class BlogResource(Resource):
    @api.marshal_list_with(blog_model)
    def get(self):
        '''GET ALL RECIPES'''
        blog_items = Blog.query.all()
        return blog_items

    @api.expect(blog_model)
    @api.marshal_with(blog_model)
    @jwt_required()
    def post(self):
        '''POST NEW RECIPE'''
        data = request.get_json()

        new_blog = Blog(
            title = data.get('title'),
            content = data.get('content')
        )

        new_blog.add()
        return new_blog, 201

@api.route('/blog/<int:id>')
class BlogResource(Resource):
    @api.marshal_with(blog_model)
    @jwt_required()
    def get(self, id):
        '''GET ONE RECIPE BY ID'''
        blog = Blog.query.get_or_404(id)
        return blog

    @api.marshal_with(blog_model)
    @jwt_required()
    def put(self, id):
        '''UPDATE RECIPE BY ID'''
        blog_to_update = Blog.query.get_or_404(id)
        data = request.get_json()
        blog_to_update.update(data.get('title'), data.get('content'))
        return blog_to_update, 204
    
    @api.marshal_with(blog_model)
    @jwt_required()
    def delete(self, id):
        '''DELETE RECIPE BY ID'''
        blog_to_delete = Blog.query.get_or_404(id)
        blog_to_delete.delete()
        return jsonify({"message": "Item deleted successfully"}), 204
