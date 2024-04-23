import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReadMailsComponent } from './read-mails.component';

describe('ReadMailsComponent', () => {
  let component: ReadMailsComponent;
  let fixture: ComponentFixture<ReadMailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ReadMailsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ReadMailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
