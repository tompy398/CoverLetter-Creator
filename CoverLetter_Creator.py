import textwrap
from fpdf import FPDF
# cl = Cover Letter
cover_letter = ''

def createCoverLetter():
    global cover_letter
    
    cl_txts = [
        'Dear Hiring Manager,\n\nMy name is ', # 1
        ', and I came across your ', # 2
        ' position at ', # 3
        ' and would like to submit my resume for your consideration. The position at ', # 4
        ' interests me as ', # 5
        '. ', # 6
        '.\n\nYour company\'s mission statement to ',  # Check if the user included a period or not (Maybe?) # 7
        ' aligns with my personal values of ',  # 8
        '. It would be personally gratifiying to work for ', # 9
        ' as ', # 10
        '.\n\nI believe I would be a good fit for ', # 11
        ' because of my ', # 12
        '; ', # 13
        '. I am looking for a company like yours where I can learn and grow with the company and apply my excellent skills in ', # 14
        ' which I developed ', # 15
        '.\n\nI also find that your work culture of ', # 16
        ' resonates with me and my personality, and is exactly what I am looking for from a company. I\'m excited about the opportunity to contribute to your company while furthering my understanding of ', # 17
        '. Thank you so much for your consideration and I hope to hear back from you soon!\n\nSincerely,\n' # 18
    ]

    input_prompt = [
        'Name', # 1
        'Job Position', # 2
        'Company', # 3
        'Company', # 4
        'Reason', # 5
        'Background Info About Yourself (Relates to Reason) (Full Sentence pwease)', # 6
        'Company Motto', # 7
        'Related Personal Value(s)', # 8
        'Company', # 9
        'Reason', # 10
        'Company', # 11
        'Reason/Experience', # 12
        'Expand on Reason/Experience', # 13
        'Relevant Skill(s)', # 14
        'Location/Experience', # 15
        'Work Culture Values', # 16
        'Skill(s) to Grow on the Job', # 17
        'Name' # 18
    ]

    print('\nWelcome to the Cover Letter Spitter!')
    print('After the program is complete, a PDF file called \'coverletter_out.pdf\' will be generated')
    print('Please enter the input according to the prompt, also don\'t use periods aka \'.\'\n-----------------------------------------------')
    print('What\'s your name?')
    applicant_name = input()
    print('What\'s the name of the company you\'re applying to?')
    company_name = input()
    print()

    for i in range(len(cl_txts)):
        cover_letter += cl_txts[i]

        if input_prompt[i] == 'Company':
            cover_letter += company_name
        elif input_prompt[i] == 'Name':
            cover_letter += applicant_name
        else:
            print('-----------------------------------------------')
            print(cover_letter + '\n')
            print('-----------------------------------------------')
            print(input_prompt[i] + ': ')
            cover_letter += input()

    print('-----------------------------------------------')
    print('FINAL RESULT:\n')
    print(cover_letter)


def text_to_pdf(text, filename):
    
    a4_width_mm = 335 #
    pt_to_mm = 0.5
    fontsize_pt = 12
    fontsize_mm = fontsize_pt * pt_to_mm
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(False)
    pdf.add_page()
    pdf.set_font(family='Arial', size=fontsize_pt)
    splitted = text.split('\n')
    pdf.ln(15)
    for line in splitted:
        lines = textwrap.wrap(line, width_text, initial_indent='              ', subsequent_indent='              ')

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')
    

if __name__ == '__main__':
    createCoverLetter()
    #print(repr(cover_letter))
    text_to_pdf(cover_letter, 'coverletter_out.pdf')
    print('\n\nPress ENTER to exit the program...')
    print('ALSO, remember that PDF')
    input()
