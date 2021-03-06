from datetime import timedelta
from http import HTTPStatus

from flask import request
from flask_jwt_extended import create_access_token

from app.models import UserModel


def login():
    try:
        data = request.get_json()
        data['email'] = data['email'].lower()

        user: UserModel = UserModel.query.filter_by(
            email=data['email']
        ).first()

        if not user:
            return {'error': 'User not found!'}, HTTPStatus.NOT_FOUND

        if not user.is_validate:
            return {'error': 'email not validate!'}, HTTPStatus.UNAUTHORIZED

        if user.verify_password(data['password']):
            data = {'id': user.id, 'name': user.name, 'email': user.email}

            accessToken = create_access_token(
                identity=data, expires_delta=timedelta(days=1)
            )
            return {'token': accessToken, 'user': data}, HTTPStatus.OK
        else:
            return {'error': 'Unauthorized'}, HTTPStatus.UNAUTHORIZED

    except KeyError:
        expected = ['email', 'password']
        obtained = [key for key in data.keys()]
        return {
            'expected': expected,
            'obtained': obtained,
        }, HTTPStatus.BAD_REQUEST
