import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NovacompraComponent } from './novacompra.component';

describe('NovacompraComponent', () => {
  let component: NovacompraComponent;
  let fixture: ComponentFixture<NovacompraComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NovacompraComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NovacompraComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
