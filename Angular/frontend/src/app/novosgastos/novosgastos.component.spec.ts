import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NovosgastosComponent } from './novosgastos.component';

describe('NovosgastosComponent', () => {
  let component: NovosgastosComponent;
  let fixture: ComponentFixture<NovosgastosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NovosgastosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NovosgastosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
