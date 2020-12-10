export default function createIteratorObject(report) {
	
}

const report = createReportObject({});
const reportWithIterator = createIteratorObject(report);
console.log('-------------------------');
console.log(typeof reportWithIterator[Symbol.iterator]);
