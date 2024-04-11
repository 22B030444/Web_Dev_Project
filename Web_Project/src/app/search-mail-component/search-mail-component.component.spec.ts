import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchMailComponentComponent } from './search-mail-component.component';

describe('SearchMailComponentComponent', () => {
  let component: SearchMailComponentComponent;
  let fixture: ComponentFixture<SearchMailComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchMailComponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SearchMailComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
