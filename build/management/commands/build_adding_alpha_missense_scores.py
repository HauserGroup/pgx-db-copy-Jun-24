
from django.core.management.base import BaseCommand
from variant.models import VepVariant
from django.conf import settings
import os
import logging
from django.db.models import Q


class Command(BaseCommand):
    help = 'Add data to the VEPVariant alphamissense column'

    # source file directory
    vep_data_dir = os.sep.join([settings.DATA_DIR, "vep_variant_data"])

    def add_arguments(self, parser):
        parser.add_argument(
            "--filename",
            action="append",
            dest="filename",
            help="Filename to import. Can be used multiple times",
        )
    logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        if options["filename"]:
            filenames = options["filename"]
        else:
            filenames = False

        # read source files
        if not filenames:
            filenames = [
                fn
                for fn in os.listdir(self.vep_data_dir)
                if fn.endswith("20231212-VariantAndAlphaMissenseScores.csv")
            ]
            print(filenames)
        count=0
        for filename in filenames:
            filepath = os.sep.join([self.vep_data_dir, filename])
            with open(filepath, "r") as f:
                lines = f.readlines()
                for i,line in enumerate(lines[1:]):
                    values=line[:-1].split(";")
                    variant_marker = values[1]
                    transcript_id = values[2]
                    am_score = values[-1]
                    # print("variant_marker = ",variant_marker)
                    # print("transcript_id = ",transcript_id)
                    # Code to add values to the new field
                    try:
<<<<<<< HEAD:build/management/commands/build_adding_alpha_missense_scores_DO.py
                        objs = VepVariant.objects.filter(
                            Q(Variant_marker=variant_marker) & Q(Transcript_ID=transcript_id)
                        )
                        if len(objs)>1:
                            print(i, " variant_marker: ", variant_marker, " transcript_id", transcript_id)
                        obj = objs[0]
=======
                        obj = VepVariant.objects.filter(
                            Q(Variant_marker=variant_marker) & Q(Transcript_ID=transcript_id)
                        )[0]
                        if len(obj)>1:
                            print(i, " variant_marker: ", variant_marker, " transcript_id", transcript_id)
>>>>>>> 5bfbe96e2d112597ba5bde39c59dbf48c4eed817:build/management/commands/build_adding_alpha_missense_scores.py
                        obj.AM_pathogenicity = am_score
                        obj.save()
                    except VepVariant.DoesNotExist:
                        # Handle the case when the object does not exist
                        print(f"Object not found for Variant_marker: {variant_marker} and Transcript_ID: {transcript_id}")
                        count+=1
        print("---- end of adding data, number of case not found: ", count)