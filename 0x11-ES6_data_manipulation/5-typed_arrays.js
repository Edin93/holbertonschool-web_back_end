export default function createInt8TypedArray(length, position, value) {
	try {
		let buffer = new Int8Array(length, position);
		buffer[0] = value;
		return buffer;

	} catch (error) {
		throw Error('Position outside range');
	}
}
