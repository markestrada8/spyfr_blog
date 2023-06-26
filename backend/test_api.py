import unittest
from main import create_app
from config import TestConfig
from extensions import db

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.init_app(self.app)
            db.create_all()

    # TEST ROUTES:
    #     TEST BASE
    #     TEST SIGNUP
    #     TEST LOGIN
    #     TEST GET ALL
    #     TEST POST
    #     TEST GET ONE
    #     TEST UPDATE
    #     TEST DELETE

    def test_root_route(self):
        test_response = self.client.get('/blog/test')

        json = test_response.json

        self.assertEqual(json, {'message': 'Test received'})


    def test_signup(self):
        signup_response = self.client.post('/auth/signup', json={
            'email': 'testuser@email.com',
            'username': 'testuser',
            'password': 'password'
        })

        self.assertEqual(signup_response.status_code, 201)


    def test_login(self):
        signup_response = self.client.post('/auth/signup', json={
            'email': 'testuser@email.com',
            'username': 'testuser',
            'password': 'password'
        })

        login_response = self.client.post('/auth/login', json={
            'email': 'testuser@email.com',
            'password': 'password'
        })

        self.assertEqual(login_response.status_code, 200)


    def test_get_all(self):
        get_all_response = self.client.get('/blog/blogs')
        self.assertEqual(get_all_response.status_code, 200)


    def test_post_new_blog(self):
        # GET TOKEN
        signup_response = self.client.post('/auth/signup', json={
            'email': 'testuser@email.com',
            'username': 'testuser',
            'password': 'password'
        })

        login_response = self.client.post('/auth/login', json={
            'email': 'testuser@email.com',
            'password': 'password'
        })
        access_token = login_response.json['access_token']

        # TEST POST (CREATE) ROUTE
        data = {
            'title': 'Test Blog',
            'content': 'This is a test blog.'
        }
        response = self.client.post('/blog/blogs', json=data, headers={'Authorization':f'Bearer {access_token}'})
        assert response.status_code == 201
        assert response.json['title'] == data['title']
        assert response.json['content'] == data['content']


    def test_get_blog_by_id(self):
        # GET TOKEN
        signup_response = self.client.post('/auth/signup', json={
            'email': 'testuser@email.com',
            'username': 'testuser',
            'password': 'password'
        })

        login_response = self.client.post('/auth/login', json={
            'email': 'testuser@email.com',
            'password': 'password'
        })
        access_token = login_response.json['access_token']

        # TEST POST (CREATE) ROUTE
        data = {
            'title': 'Test Blog',
            'content': 'This is a test blog.'
        }
        response = self.client.post('/blog/blogs', json=data, headers={'Authorization':f'Bearer {access_token}'})
        blog_id = 1
        response = self.client.get(f'/blog/blog/{blog_id}', headers={'Authorization':f'Bearer {access_token}'})

        assert response.status_code == 200


    def test_update_blog_by_id(self):
        # GET TOKEN
        signup_response = self.client.post('/auth/signup', json={
            'email': 'testuser@email.com',
            'username': 'testuser',
            'password': 'password'
        })

        login_response = self.client.post('/auth/login', json={
            'email': 'testuser@email.com',
            'password': 'password'
        })
        access_token = login_response.json['access_token']

        # TEST POST (CREATE) ROUTE
        data = {
            'title': 'Test Blog',
            'content': 'This is a test blog.'
        }
        response = self.client.post('/blog/blogs', json=data, headers={'Authorization':f'Bearer {access_token}'})

        # TEST UPDATE ROUTE
        blog_id = 1
        data = {
            'title': 'Updated Blog Title',
            'content': 'This is the updated content of the blog.'
        }
        response = self.client.put(f'/blog/blog/{blog_id}', json=data, headers={'Authorization':f'Bearer {access_token}'})
        assert response.status_code == 200


    def test_delete_blog_by_id(self):
        # GET TOKEN
        signup_response = self.client.post('/auth/signup', json={
            'email': 'testuser@email.com',
            'username': 'testuser',
            'password': 'password'
        })

        login_response = self.client.post('/auth/login', json={
            'email': 'testuser@email.com',
            'password': 'password'
        })
        access_token = login_response.json['access_token']

        # TEST POST (CREATE) ROUTE
        data = {
            'title': 'Test Blog',
            'content': 'This is a test blog.'
        }
        response = self.client.post('/blog/blogs', json=data, headers={'Authorization':f'Bearer {access_token}'})

        # TEST DELETE ROUTE
        blog_id = 1
        data = {
            'title': 'Updated Blog Title',
            'content': 'This is the updated content of the blog.'
        }
        blog_id = 1
        response = self.client.delete(f'/blog/blog/{blog_id}', headers={'Authorization':f'Bearer {access_token}'})
        assert response.status_code == 200


    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()
