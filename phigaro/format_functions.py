import csv


def phages_to_out(find_res, f):
    for scaffold, npn, phages in find_res:
        for phage in phages:
            phage_type = 'profage' if phage['is_pro_phage'] else 'phage'
            ar = ' (ar)' if phage['ar_here'] else ''

            f.write('>{}: {}{}\n'.format(
                scaffold, phage_type, ar
            ))
            f.write('{}\n'.format(npn[phage['start']: phage['end']]))


def phages_to_csv(find_res, f):
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(('scaffold', 'start', 'end', 'type', 'ar_here'))
    for scaffold, npn, phages in find_res:
        for phage in phages:
            phage_type = 'profage' if phage['is_pro_phage'] else 'phage'
            ar = 'AR' if phage['ar_here'] else 'NO AR'

            row = (scaffold, phage['start'], phage['end'], phage_type, ar)
            writer.writerow(row)
