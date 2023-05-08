function displayArrayResponse() {
    // Use fetch to retrieve the array response from the backend
    fetch('/city')
      .then(response => response.json())
      .then(data => {
        // Get the HTML element where we want to display the array
        const arrayElement = document.getElementById('route-array');
  
        // Use map() to loop through the array and create a new array of list item elements
        const listItems = data.map(item => `<li>${item}</li>`);
  
        // Set the innerHTML of the HTML element to the list items
        arrayElement.innerHTML = `<ul>${listItems.join('')}</ul>`;
      })
      .catch(error => {
        console.error('Error fetching array response:', error);
      });
  }
  