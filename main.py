from pyscript import display, document

def add_member(e):
    document.getElementById('result').innerHTML = ' '
    grade7 = {'Mckenna Grace', 'Walker Scobell', 'Ariana Greenblatt'}
    grade8 = {'Millie Bobby Brown', 'Jenna Ortega', 'Peyton List'}
    grade9 = {'Maya Hawke', 'Elle Fanning', 'Florence Pugh'}
    grade10 = {'Matt Damon', 'Anne Hathaway', 'Robert Pattinson'}
    
    firstname = document.getElementById('first_name').value
    surname = document.getElementById('last_name').value
    full_name = firstname + ' ' + surname

    og_members = grade7.union(grade8 | grade9 | grade10)
    og_members.add(full_name)
    display(og_members, target='results')

    display("Club members:", len(og_members), target='results')
