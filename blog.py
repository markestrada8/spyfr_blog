from flask import request, jsonify
from flask_restx import Resource, fields, Namespace, marshal
from flask_jwt_extended import jwt_required

from models import Blog


# ESTABLISH Blog NAMESPACE
blog_ns = Namespace('blog', description='Namespace for blog')

# MODEL SERIALIZER (INTERFACE FOR REQUEST / RESPONSE - NOT STRICTLY ENFORCED)
blog_model = blog_ns.model(
    "Blog",
    {
        "id": fields.Integer(),
        "title": fields.String(),
        "content": fields.String(),
        "created_at": fields.DateTime()
    }
)

blog_message_response_model = blog_ns.model(
    "Blog Message Response",
    {
        "message": fields.String(),
    }
)

@blog_ns.route('/test')
class TestResource(Resource):
    def get(self):
        return jsonify({"message": "Test received"})

@blog_ns.route('/blogs')
class BlogResource(Resource):
    @blog_ns.marshal_list_with(blog_model)
    def get(self):
        '''GET ALL BLOGS'''
        # print('Request headers: ', request.headers)
        blog_items = Blog.query.all()
        return blog_items

    @blog_ns.expect(blog_model)
    @blog_ns.marshal_with(blog_model)
    @jwt_required()
    def post(self):
        '''POST NEW BLOG'''
        data = request.get_json()

        new_blog = Blog(
            title = data.get('title'),
            content = data.get('content')
        )

        new_blog.add()
        return marshal(new_blog, blog_model), 201

@blog_ns.route('/blog/<int:id>')
class BlogResource(Resource):
    # @blog_ns.expect(blog_model)
    @blog_ns.marshal_with(blog_model)
    # @jwt_required()
    def get(self, id):
        '''GET ONE BLOG BY ID'''
        blog = Blog.query.get_or_404(id)
        return marshal(blog, blog_model), 200

    # @blog_ns.expect(blog_model)
    @blog_ns.marshal_with(blog_message_response_model)
    @jwt_required()
    def put(self, id):
        '''UPDATE BLOG BY ID'''
        blog_to_update = Blog.query.get_or_404(id)
        data = request.get_json()
        blog_to_update.update(data.get('title'), data.get('content'))
        response_data = Blog.query.get_or_404(id)

        return marshal({"message": "Blog updated successfully"}, blog_message_response_model), 200

    @blog_ns.marshal_with(blog_model)
    @jwt_required()
    def delete(self, id):
        '''DELETE BLOG BY ID'''
        blog_to_delete = Blog.query.get_or_404(id)
        blog_to_delete.delete()

        return marshal({"message": "Blog deleted successfully"}, blog_message_response_model), 200
