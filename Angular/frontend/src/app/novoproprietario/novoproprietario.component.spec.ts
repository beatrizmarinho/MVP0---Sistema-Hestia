import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NovoproprietarioComponent } from './novoproprietario.component';

describe('NovoproprietarioComponent', () => {
  let component: NovoproprietarioComponent;
  let fixture: ComponentFixture<NovoproprietarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NovoproprietarioComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NovoproprietarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
