import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const result = await Promise.all([
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

  return result;
}
