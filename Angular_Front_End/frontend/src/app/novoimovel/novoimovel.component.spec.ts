import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NovoimovelComponent } from './novoimovel.component';

describe('NovoimovelComponent', () => {
  let component: NovoimovelComponent;
  let fixture: ComponentFixture<NovoimovelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NovoimovelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NovoimovelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
