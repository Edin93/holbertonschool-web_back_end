import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
	try {
		const user = createUser();
		const photo = uploadPhoto();

		return {
			photo: photo.then((data) => data),
			user: user.then((data) => data)
		};
	}
	catch (e) {
		return {
			photo: null,
			user: null
		}
	}
}
