describe('My First Test', function() {
    it('Visits the site', function() {
      cy.visit('http://localhost:8081/')
    })
  })

describe('Cheking', function() {
  it('Checks', function() {
    //cy.get('img').should('contain','/frontend/src/assets/logo.png')
    cy.get('#app > div > :nth-child(1)').should('contain','Home page')
    cy.get('button').should('contain','New random number')
  })

  it('Click', function () {

    cy.get('button').click()

  })
})
