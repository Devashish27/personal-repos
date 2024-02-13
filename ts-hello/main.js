// function log(message) {
//   console.log(message);
// }
// var message = 'Hello world';
// log(message);
// var number = 1;
// let count = 2;
// function doSomething() {
// for (var i = 0; i < 5; i ++) {
//   for (let i = 0; i < 5; i ++) {
//     console.log(i);
//   }
//   console.log('Finally: ' + i);
// }
// doSomething();
// let count = 5;
// count = 'a';
// let a: number;
// a = 1;
// a = true;
// a = 'a';
// let b: boolean;
// let c: string;
// let d: any;
// let e: number[] = [1, 2, 3];
// let f: any[] = [1, true, 'a', false];
// const ColorRed = 0;
// const ColorGreen = 1;
// const ColorBlue = 2;
// enum Color { Red = 0, Green = 1, Blue = 2 };
// let backgroundColor: Color = Color.Red;
// let message;
// message = 'abc';
// let endsWithC = (<string>message).endsWith('c');
// let alternativeWay = (message as string).endsWith('c');
// let log = function(message1) {
//   console.log(message1);
// }
// let doLog = (message2) => console.log(message2);
// interface Point {
//   x: number,
//   y: number,
//   draw: () => void
// }
var Point = /** @class */ (function () {
    function Point() {
    }
    Point.prototype.draw = function () {
        console.log('X: ' + this.x + ', Y: ' + this.y);
    };
    Point.prototype.getDistance = function (another) {
        // ...
    };
    return Point;
}());
// let drawPoint = (point: {x: number, y: number}) => {
// let drawPoint = (point: Point) => {
// }
// let getDistance = (pointA: Point, pointB: Point) => {
//   // ...
// }
// drawPoint({
//   x: 1,
//   y: 2
// })
var point = new Point();
point.x = 1;
point.y = 2;
point.draw();
