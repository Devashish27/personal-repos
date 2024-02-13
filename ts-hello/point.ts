export 
class Point {

  constructor(public x?: number, private y?: number){
  }

  draw() {
    console.log('X: ' + this.x + ', Y: ' + this.y);
  }
}
