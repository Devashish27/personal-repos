import { Component} from '@angular/core';
import { CoursesService } from './course/courses.service';

@Component({
  selector: 'courses', // <rating>
  // template: '<h2>{{ "Title: " + title }}</h2>'
  // template: '<h2>{{ getTitle() }}</h2>'  // String inter pollation...
  template: `
      <h2>{{ title }}</h2>
      <ul>
          <li *ngFor="let course of courses">
              {{ course }}
          </li>
      </ul>
  `
})

export class CoursesComponent
{
  title = "List of Courses ";

  // getTitle() {
  //   return this.title;
  // }
  courses;

  constructor(service: CoursesService) {
    // let service = new CoursesService();
    this.courses = service.getCourses();

  }

}

