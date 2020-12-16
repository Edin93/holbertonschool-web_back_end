import uploadPhoto from './5-photo-reject';
import signUpUser from './4-user-promise';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    uploadPhoto(fileName),
    signUpUser(firstName, lastName),
  ]).then((state, value) => {
    console.log({
      state,
      value,
    });
  });
}
