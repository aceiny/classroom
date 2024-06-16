-- AlterTable
ALTER TABLE "File" ADD COLUMN     "coursworkId" TEXT,
ADD COLUMN     "submissionId" TEXT;

-- AddForeignKey
ALTER TABLE "File" ADD CONSTRAINT "File_submissionId_fkey" FOREIGN KEY ("submissionId") REFERENCES "Submission"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "File" ADD CONSTRAINT "File_coursworkId_fkey" FOREIGN KEY ("coursworkId") REFERENCES "Courswork"("id") ON DELETE SET NULL ON UPDATE CASCADE;
