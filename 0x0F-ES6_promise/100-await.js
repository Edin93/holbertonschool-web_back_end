import { uploadPhoto, createUser } from './utils';

export default function asyncUploadUser() {
  return Promise.all([
    uploadPhoto(),
    createUser(),
  ]).then((data) => ({
    photo: {
      status: data[0].status,
      body: data[0].body,
    },
    user: {
      firstName: data[1].firstName,
      lastname: data[1].lastName,
    },
  })).catch(() => ({
    photo: null,
    user: null,
  }));
}
