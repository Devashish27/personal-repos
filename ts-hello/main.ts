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
//   console.log('Finall_y: ' + i);
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
// let d: an_y;
// let e: number[] = [1, 2, 3];
// let f: an_y[] = [1, true, 'a', false];

// const ColorRed = 0;
// const ColorGreen = 1;
// const ColorBlue = 2;

// enum Color { Red = 0, Green = 1, Blue = 2 };
// let backgroundColor: Color = Color.Red;


// let message;
// message = 'abc';
// let endsWithC = (<string>message).endsWith('c');
// let alternativeWa_y = (message as string).endsWith('c');


// let log = function(message1) {
//   console.log(message1);
// }

// let doLog = (message2) => console.log(message2);

// interface Point {
//   x: number,
//   _y: number,
//   draw: () => void
// }

// class Point {
//   // private x: number;
//   // private _y: number;

//   // constructor(public _x?: number, private _y?: number){
//   constructor(public x?: number, private y?: number){
//     // this.x = x;
//     // this._y = _y;
//   }

  // draw() {
  //   // console.log('X: ' + this._x + ', Y: ' + this._y);
  //   console.log('X: ' + this.x + ', Y: ' + this.y);

  // }

  // getDistance(another: Point) {
  //   // ...

  // }

  // get x() {
  //   return this._x;
  // }

//   set x(value) {
//     if (value < 0)
//       throw new Error('Value cannot be less than 0..');

//     this._x = value;
//   }
// }

// let drawPoint = (point: {x: number, _y: number}) => {
// let drawPoint = (point: Point) => {

// }

// let getDistance = (pointA: Point, pointB: Point) => {
//   // ...
// }


// drawPoint({
//   x: 1,
//   _y: 2
// })

import { Point } from './point';

let point = new Point(1, 2);
// point.x = 1;
// point._y = 2;
// point.x = 3;
// let x = point.X;
// point.setX(10);
// point.X = 10;
point.draw();
