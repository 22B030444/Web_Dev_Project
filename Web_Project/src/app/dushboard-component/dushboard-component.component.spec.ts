import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DushboardComponentComponent } from './dushboard-component.component';

describe('DushboardComponentComponent', () => {
  let component: DushboardComponentComponent;
  let fixture: ComponentFixture<DushboardComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DushboardComponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DushboardComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
